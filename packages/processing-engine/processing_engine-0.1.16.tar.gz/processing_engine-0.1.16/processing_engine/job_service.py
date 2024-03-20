from typing import List
import psycopg2

import logging
import psycopg2.extras
from processing_engine.dda_models import LogMessage
from processing_engine.class_helpers import Utils

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

class JobService():
    """
    Tracks errors and log Messages, single instance of connection requirements, passed around. Gets reset and instantiated by the Enhancement Manager each time a new event is processed.
    To keep track of:
    - DBengine: DBengine to be used to query the database.
    - processing_guid

    - last_error_message
    - last_error_time

    - item count
    - s3_key
    - integration_name
    - integration_version

    - adapter used.
    - organization_guid

    - array of log_messages

    Methods:
    - Filter count of error messages
    - Add Error Message



    Messages Log Tracking requires of.
    - log_date
    - event_guid
    - log_type
    - log_message
    - log_detail
    """

    def __init__(self,  
                 username: str, password: str, host: str, database: str,
                 organization_guid: str, connector_guid: str, processing_guid: str,
                 integration_name: str, job_parameters: dict, cloudwatchlog_message_function=None):
        
        # Key Parameters: postgresql credentials
        self.connection = psycopg2.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )

        self.cursor = self.connection.cursor(
            cursor_factory=psycopg2.extras.DictCursor
        )

        self.cursor.execute("SELECT id FROM organization WHERE guid = %s", (organization_guid,))

        organization_id = self.cursor.fetchone()
        if organization_id is None:
            raise ValueError("Organization not found")

        self.connector_guid = connector_guid

        # For processiing type, you do need to 

        self.organization_guid = organization_guid
        self.processing_guid = processing_guid
        self.integration_name = integration_name

        self.integration_version = Utils.SafeParse(job_parameters, 'integration_version')
        self.s3_key = Utils.SafeParse(job_parameters, 's3_key')
        self.item_count = Utils.SafeParse(job_parameters, 'item_count')
        self.adapter = Utils.SafeParse(job_parameters, 'adapter') # Adapter used to process the data.
        self.event_date = Utils.SafeParse(job_parameters, 'event_date')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.log_messages: List[LogMessage] = []
        self.last_error_message = None
        self.last_error_time = None
        self.cloudwatchlog_message_function = None

        self.logger.info(f"Job Service Initialized for: {self.processing_guid}")

    def addLogMessage(self, log_message: str, log_detail: str, log_type: str = 'Error', log_console: bool = True):
        # print("==================================================================")
        # print(f"Log Message: {log_message} - {log_detail}")
        self.log_messages.append(LogMessage(log_type, log_message, log_detail))
        if log_console:
            # self.logger.info(f"Log Message: {log_message} - {log_detail}")
            pass

        if self.cloudwatchlog_message_function is not None:
            self.cloudwatchlog_message_function(log_message, log_detail, log_type)

        if log_type == 'Error':
            self.last_error_message = log_message
            self.last_error_time = Utils.getNow()
            logging.error(log_message, log_detail)
        else:
            # logging.info(log_message, log_detail)
            pass
        
    def startProcessingStatus(self):
        # SELECT IF exists, Update, otherwise insert.
        select_query = """
            SELECT id FROM processing_tracker WHERE processing_guid = %s
        """
        self.cursor.execute(select_query, (self.processing_guid,))
        
        processing_id = self.cursor.fetchone()

        if processing_id is None:
            query = """
            INSERT INTO processing_tracker (
                processing_guid,
                status,
                source_guid,
                s3_key,
                connector_guid,
                organization_guid,
                integration_name,
                integration_version,
                source_date,
                task,
                start_time,
                received_time,
                item_count
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            """

            values = [
                self.processing_guid,
                'PROCESSING',
                self.processing_guid,
                self.s3_key,
                self.connector_guid,
                self.organization_guid,
                self.integration_name,
                self.integration_version,
                self.event_date,
                'TIMESLOT PROCESSING',
                Utils.getNow(),
                Utils.getNow(),
                self.item_count
            ]

            self.cursor.execute(query, tuple(values))

            self.connection.commit()
            self.logger.info(f"Processing Started for: {self.processing_guid}")
        else:
            self.changeProcessingStatus('RE-PROCESSING')
            self.logger.info(f"Processing Re-Started for: {self.processing_guid}")

        
    def changeProcessingStatus(self, status: str):
        self.cursor.execute(
            "UPDATE processing_tracker SET status = %s WHERE processing_guid = %s",
            (status, self.processing_guid)
        )

        self.connection.commit()

    def endProcessingStatus(self):
        # Calculate the count of errors:
        _error_messages = [x for x in self.log_messages if x.log_type == 'Error']
        count_error_messages = len(_error_messages)

        end_time = Utils.getNow()
        query = "UPDATE processing_tracker SET status = %s, end_time = %s"

        # Constructing values for the first part of the query
        values = ['COMPLETE', end_time]

        last_error_message = self.last_error_message
        if last_error_message is not None:
            last_error_log = _error_messages[-1] if count_error_messages > 0 else None
            last_error_datetime = last_error_log.log_date.strftime('%Y-%m-%d %H:%M:%S') if last_error_log is not None else None

            # Adding error-related fields to the query if there's an error message
            query += """
                , error_count = %s,
                last_error_message = %s,
                last_error_time = %s
            """

            # error_sample = %s

            # Constructing values for the error-related fields
            values.extend([count_error_messages, last_error_message, last_error_datetime])

        # Adding the WHERE clause
        query += " WHERE processing_guid = %s"

        # Adding the processing_guid value to the values list
        values.append(self.processing_guid)
        print("Query")
        print(query)
        # Executing the query
        self.cursor.execute(query, tuple(values))


        self.connection.commit()
        self.logger.info(f"Processing Ended for: {self.processing_guid}")

    # destroy overwrite. ensure that the connection is closed after the processing is done.
    def __del__(self):
        self.connection.close()
        self.cursor.close()
        self.connection = None
        self.cursor = None
