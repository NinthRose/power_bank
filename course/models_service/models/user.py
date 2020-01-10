import datetime

from pytz import utc

from course.models import User
from course.models_service.models_controller import models_lock


def models_add_user(name, phone, password):
    with models_lock:
        user = User.objects.create(name=name, phone=phone, password=password)
        return user.to_dict()


def models_user_exist(phone):
    with models_lock:
        try:
            user = User.objects.get(phone=phone)
            return user.to_dict()
        except:
            return False


def models_load_user(phone, instance4foreign_key=None):
    with models_lock:
        user = User.objects.get(phone=phone)
    if instance4foreign_key:
        return user
    else:
        return user.to_dict(True)


def models_update_login(phone):
    with models_lock:
        user = User.objects.get(phone=phone)
        user.last_login = datetime.datetime.now(utc)
        user.save()
