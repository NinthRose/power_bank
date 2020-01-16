import datetime

from pytz import utc

from course.common.utils.md5 import to_md5
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


def models_reset_user(phone, name, password):
    with models_lock:
        user = User.objects.get(phone=phone)
        if name:
            user.name = name
        if password:
            user.password = to_md5(password)
        user.save()


def models_update_login(phone):
    with models_lock:
        user = User.objects.get(phone=phone)
        user.last_login = datetime.datetime.now(utc)
        user.save()


def models_search_user(keyword, page_size, page_num):
    with models_lock:
        users = User.objects.all()
        if keyword:
            users = users.filter(phone__contains=keyword)
        users = users[page_size * (page_num - 1):page_size * page_num]
        users = list(users.values('phone', 'name', 'last_login', 'ctime'))
        for u in users:
            for key, value in u.items():
                if isinstance(value, datetime.datetime):
                    u[key] = str(value)
        return users


def models_page_user(keyword, page_num):
    with models_lock:
        users = User.objects.all()
        if keyword:
            users = users.filter(phone__contains=keyword)
        page = users.count() / page_num
        if page > int(page):
            page = int(page) + 1
        else:
            page = int(page)
        return page
