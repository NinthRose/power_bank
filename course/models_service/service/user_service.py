from course.common.exceptions.models.user_exception import PowerBankUserException
from course.common.utils.md5 import to_md5
from course.models_service.models.user import models_user_exist, models_add_user, models_load_user, models_update_login, \
    models_reset_user


def user_exist(phone):
    return models_user_exist(phone)


def add_user(phone, name, password):
    user = models_user_exist(phone)
    if user:
        raise PowerBankUserException('手机号已注册：{}，用户名为{}'.format(phone, user['name']))
    return models_add_user(name, phone, to_md5(password))


def reset_user(phone, name, password):
    models_reset_user(phone, name, password)


def load_user(phone, instance4foreign_key=None):
    return models_load_user(phone, instance4foreign_key)


def user_login_update(phone):
    models_update_login(phone)
