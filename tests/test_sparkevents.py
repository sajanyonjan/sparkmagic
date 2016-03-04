from remotespark.utils.sparkevents import SparkEvents
import remotespark.utils.constants as constants
from remotespark.utils import utils
from nose.tools import with_setup
from mock import MagicMock

def _setup():
    global spark_events, guid, time_stamp

    spark_events = SparkEvents()
    spark_events.handler = MagicMock()
    SparkEvents.get_utc_date_time = MagicMock()
    time_stamp = spark_events.get_utc_date_time()
    guid = utils.generate_uuid()

def _teardown():
    pass

@with_setup(_setup, _teardown)
def test_emit_session_creation_start_event():

    language = constants.SESSION_KIND_SPARK
    event_name = constants.SESSION_CREATION_START_EVENT

    kwargs_list = [("TimeStamp", time_stamp), ("EventName", event_name), ("SessionGuid", guid),
                ("SparkLanguage", language)]

    spark_events.emit_session_creation_start_event(guid, language)
    spark_events.get_utc_date_time.assert_called_with()
    spark_events.handler.handle_event.assert_called_once_with(kwargs_list)

@with_setup(_setup, _teardown)
def test_emit_session_creation_end_event():

    language = constants.SESSION_KIND_SPARK
    event_name = constants.SESSION_CREATION_END_EVENT
    status = constants.BUSY_SESSION_STATUS
    session_id = 0

    kwargs_list = [("TimeStamp", time_stamp), ("EventName", event_name), ("SessionGuid", guid),
                ("SparkLanguage", language), ("SessionId", session_id), ("Status:", status)]

    spark_events.emit_session_creation_end_event(guid, language, session_id, status)
    spark_events.get_utc_date_time.assert_called_with()
    spark_events.handler.handle_event.assert_called_once_with(kwargs_list)