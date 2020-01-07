import datetime

from pytz import utc

from course.common.configuration.config_parser import orca_config
from course.models_service.models.session import models_add_session, models_load_session, models_remove_session, \
    models_update_session


def add_session(user):
    return models_add_session(user)


def is_illegal_session(session_id: str):
    session_time = orca_config.get_config('config', 'SESSION_TIMEOUT', int)
    session = models_load_session(session_id)
    b = datetime.datetime.now(tz=utc)
    a = session.mtime.replace(tzinfo=utc)
    stime = (b - a).total_seconds()
    if stime > session_time:
        models_remove_session(session)
        return True
    else:
        models_update_session(session)
        return False


def remove_session(session):
    models_remove_session(session)
