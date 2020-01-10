from course.common.exceptions.models.user_exception import PowerBankUserException
from course.common.utils.md5 import to_md5
from course.models_service.models.user import models_user_exist, models_add_user, models_load_user, models_update_login


def user_exist(phone):
    return models_user_exist(phone)


def add_user(name, phone, password):
    user = models_user_exist(phone)
    if user:
        raise PowerBankUserException('手机号已注册：{}，用户名为{}'.format(phone, user['name']))
    return models_add_user(name, phone, to_md5(password))


def load_user(phone, instance4foreign_key=None):
    return models_load_user(phone, instance4foreign_key)


def user_login_update(phone):
    models_update_login(phone)
