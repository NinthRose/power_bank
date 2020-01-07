import time

import datetime

from pytz import utc

from course.common.utils.md5 import to_md5
from course.models import Session
from course.models_service.constants.models import models_constant
from course.models_service.models_controller import models_lock


def models_add_session(user: str):
    session_id = to_md5(str(time.time()))
    with models_lock:
        Session.objects.create(session=session_id, user=user, mtime=datetime.datetime.now(utc))
    return session_id


def models_remove_session(session: str):
    with models_lock:
        if models_constant.is_id(session):
            Session.objects.get(session=session).delete()
        else:
            session.delete()


def models_load_session(session: str):
    with models_lock:
        session = Session.objects.get(session=session)
        return session


def models_update_session(session: str):
    with models_lock:
        if models_constant.is_id(session):
            session = Session.objects.get(session=session)
        session.mtime = datetime.datetime.now(utc)
        session.save()
