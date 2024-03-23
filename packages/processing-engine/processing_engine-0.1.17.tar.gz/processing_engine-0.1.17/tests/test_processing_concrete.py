
from processing_engine.dda_models import *
from processing_engine.job_service import *
from processing_engine.processing_abstract import *
from processing_engine.processing_concrete import *
from processing_engine.adapters import *


import pytest
import json
import pprint

# pre test fixture
class TestProcessingConcrete:
    @pytest.fixture(scope='function')
    def job_service(self):
        job_service = JobService(
            username="postgres",
            password="dDueller123araM=!",
            host="test-ddanalytics-rds-v2.cpcwi20k2qgg.us-east-1.rds.amazonaws.com",
            database="v1_2",
            organization_guid="0238bfa6-2a89-42fe-8a67-fde4c80391ea",
            connector_guid="4c374db5-8e37-428e-b988-92ce9879165a",
            processing_guid="65dc302d-d591-4634-a531-a5eae45e182b",
            integration_name="Salesforce",
            job_parameters={}
        )
        return job_service


    def test_timeslotprocessing_integration_salesforce_splitevents(self, job_service):
        """
        Tests if timeslots are defined correctly.
        """

        timeslot_processing = TimeslotProcessing(job_service)
        salesforce_integration_adapter = SalesforceIntegrationAdapter()
        sample_events = json.load(open('tests/data/events_sf.json'))

        adapted_events: List[EventData] = salesforce_integration_adapter.adapt(sample_events, job_service)
        listEvents, listTimeslot = timeslot_processing.splitEvents(adapted_events)
        print("=========== Split Salesforce Event Sample ============")
        pprint.pprint(listEvents[0].__dict__)
        print("=========== Split Salesforce Timeslot Sample ============")
        pprint.pprint(listTimeslot[0].__dict__)
    
    def test_timeslotprocessing_integration_windows_splitevents(self, job_service):
        """
        """

        timeslot_processing = TimeslotProcessing(job_service)
        windows_integration_adapter = WindowsIntegrationAdapter()
        sample_events = json.load(open('tests/data/events_windows.json'))

        adapted_events: List[EventData] = windows_integration_adapter.adapt(sample_events, job_service)

        print("=========== Split Windows Event Sample ============")
        pprint.pprint(adapted_events[0].__dict__)

        listEvents, listTimeslot = timeslot_processing.splitEvents(adapted_events)
        print("=========== Split Windows Event Sample ============")
        pprint.pprint(listEvents[0].__dict__)
        print("=========== Split Windows Timeslot Sample ============")
        pprint.pprint(listTimeslot[0].__dict__)

    def test_timeslotprocessing_integration_email_events(self, job_service):
        """
        """

        timeslot_processing = TimeslotProcessing(job_service)
        email_integration_adapter = EmailIntegrationAdapter()
        sample_events = json.load(open('tests/data/events_email.json'))

        adapted_events: List[EventData] = email_integration_adapter.adapt(sample_events, job_service)

        print("=========== Content of Adapted Email Event Sample ============")
        pprint.pprint(adapted_events[0].__dict__)

        listEvents, listTimeslot = timeslot_processing.splitEvents(adapted_events)
        print("=========== Split Email Event Sample ============")
        pprint.pprint(listEvents[0].__dict__)
        print("=========== Split Email Timeslot Sample ============")
        pprint.pprint(listTimeslot[0].__dict__)

    def test_timeslotprocessing_integration_chrome_events_(self, job_service):
        """
        """
            
        timeslot_processing = TimeslotProcessing(job_service)
        chrome_integration_adapter = ChromeIntegrationAdapter()
        sample_events = json.load(open('tests/data/events_chrome.json'))

        adapted_events: List[EventData] = chrome_integration_adapter.adapt(sample_events, job_service)

        print("=========== Content of Adapted Chrome Event Sample ============")
        pprint.pprint(adapted_events[0].__dict__)

        listEvents, listTimeslot = timeslot_processing.splitEvents(adapted_events)
        print("=========== Split Chrome Event Sample ============")
        pprint.pprint(listEvents[0].__dict__)
        print("=========== Split Chrome Timeslot Sample ============")
        pprint.pprint(listTimeslot[0].__dict__)

    def test_timeslotprocessing_durationcon_salesforce_split_events(self, job_service):
        """
        Tests if the timeslots are correctly split.
        (duration of 170, 300, 606, 220, 3600) from salesforce: Total combine seconds: 4896
        Which is equal to: 81 minutes()

        """

        timeslot_processing = TimeslotProcessing(job_service)
        salesforce_integration_adapter = SalesforceIntegrationAdapter()
        sample_events = json.load(open('tests/data/events_sf_duration.json'))

        adapted_events: List[EventData] = salesforce_integration_adapter.adapt(sample_events, job_service)
        listEvents: List[Event]
        listTimeslot: List[Timeslot] 
        listEvents, listTimeslot = timeslot_processing.splitEvents(adapted_events)
        print("=========== Split Event Sample ============")
        print('Expected 5 events; Events count:', len(listEvents))
        pprint.pprint(listEvents[0].__dict__)
        
        print("\n\n\n=========== Split Timeslot Sample ============")
        print('Expected more than 5 timeslots; timeslots count:', len(listTimeslot))
        print("\n\n\n=========== Split Timeslot 1 ============")
        pprint.pprint(listTimeslot[0].__dict__)
        a_localts1 = listTimeslot[0].tl1
        a_ts1 = listTimeslot[0].ts1
        a_month = listTimeslot[0].month
        a_year = listTimeslot[0].year


        print("\n\n\n=========== Split Timeslot 2 ============")
        pprint.pprint(listTimeslot[1].__dict__)
        b_localts1 = listTimeslot[1].tl1
        b_ts1 = listTimeslot[1].ts1
        b_month = listTimeslot[1].month
        b_year = listTimeslot[1].year

        assert a_localts1 == b_localts1 - 1
        assert a_ts1 == b_ts1 - 1
        assert a_month == b_month
        assert a_year == b_year

        # Assert that there should be more or equal than 81 timeslots
        assert len(listTimeslot) >= 81

    def test_timeslotprocessing_publish_events(self, job_service):
        """
        Tests if the timeslots are correctly split.
        """

        timeslot_processing = TimeslotProcessing(job_service)
        salesforce_integration_adapter = SalesforceIntegrationAdapter()
        sample_events = json.load(open('tests/data/events_sf_duration.json'))

        adapted_events: List[EventData] = salesforce_integration_adapter.adapt(sample_events, job_service)
        listEvents: List[Event]
        listTimeslot: List[Timeslot]
        
        print("=========== list of Events before collapsing ============")
        print('len of listEvents:', len(adapted_events))
        adapted_events = timeslot_processing.collapseEventsSimilarEventGUID(adapted_events)
        print("=========== list of Events aftercollapsing ============")
        print('len of listEvents:', len(adapted_events))

        listEvents, listTimeslot = timeslot_processing.splitEvents(adapted_events)
        

        print("=========== Received the following list of Events ============")
        print('len of listEvents:', len(listEvents))
        # attmpt to publish each.
        timeslot_processing.publishEvents(listEvents)
        # timeslot_processing.publishTimeslots(listTimeslot)

    def test_timeslotprocessing_publish_timeslots(self, job_service):
        """
        Tests if the timeslots are correctly split.
        """

        timeslot_processing = TimeslotProcessing(job_service)
        salesforce_integration_adapter = SalesforceIntegrationAdapter()
        sample_events = json.load(open('tests/data/events_sf_duration.json'))

        adapted_events: List[EventData] = salesforce_integration_adapter.adapt(sample_events, job_service)
        listEvents: List[Event]
        listTimeslot: List[Timeslot]
        listEvents, listTimeslot = timeslot_processing.splitEvents(adapted_events)

        # attmpt to publish each.
        # timeslot_processing.publishEvents(listEvents)
        timeslot_processing.publishTimeslots(listTimeslot)

    def test_timeslotprocessing_timeslot_windows_interactions(self, job_service):
        """
        Tests if the Interactions at timeslots are correctly split.

        If the first event is:

         {
            "event_date": "2023-11-07T18:34:56.961Z",
            "event_end_date": "2023-11-07T18:34:56.961Z",
            "window_title": "pgAdmin 4 (PID: 20392)",
            "name": "pgAdmin4",
            "span_guid": "9ce056cd-9127-4dca-afde-a73ff636f01e",
            "description": null,
            "keypresses": 10,
            "mouseclicks": 3,
            "windows_pid": "20392",
            "id": 0,
            "guid": "82a2a911-0404-417e-8e0f-2704398c0d38",
            "event_type": "WIN_APP_ACTIVE",
            "actor": "AzureAD\\NelsonWang"
        },

        Should result in:

        The first timeslot expected shoul be:
        
        {
            ...
            mouse_clicks: 3,
            keystrokes: 10,
            minute: 34,
            hour: 18,
        }

        """

        timeslot_processing = TimeslotProcessing(job_service)
        windows_integration_adapter = WindowsIntegrationAdapter()
        sample_events = [
            {
                "event_date": "2023-11-07T18:34:56.961Z",
                "event_end_date": "2023-11-07T18:34:56.961Z",
                "window_title": "pgAdmin 4 (PID: 20392)",
                "name": "pgAdmin4",
                "span_guid": "9ce056cd-9127-4dca-afde-a73ff636f01e",
                "description": None,
                "interactions": [
                    {
                        "date": "2023-11-07T18:34", 
                        "key": 5,
                        "mouse": 3 
                    },
                    {
                        "date": "2023-11-07T18:35", 
                        "key": 5,
                    }
                ],
                "windows_pid": "20392",
                "id": 0,
                "guid": "82a2a911-0404-417e-8e0f-2704398c0d38",
                "event_type": "WIN_APP_ACTIVE",
                "actor": "AzureAD\\NelsonWang"
            }
        ]

        adapted_events: List[EventData] = windows_integration_adapter.adapt(sample_events, job_service)
        
        print("=========== Adapted Windows Event ============")
        pprint.pprint(adapted_events[0].__dict__)
        
        listEvents: List[Event]
        listTimeslot: List[Timeslot]

        listEvents, listTimeslot = timeslot_processing.splitEvents(adapted_events)
        
        print("=========== Received First Timeslot ============")
        pprint.pprint(listTimeslot[0].__dict__)

        assert listTimeslot[0].mouse_clicks == 3
        assert listTimeslot[0].keystrokes == 5
        assert listTimeslot[0].minute == 34
        assert listTimeslot[0].hour == 18








