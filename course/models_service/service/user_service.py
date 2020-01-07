from course.common.exceptions.models.user_exception import PowerBankUserException
from course.common.utils.md5 import to_md5
from course.models_service.models.user import models_user_exist, models_add_user, models_load_user, models_update_login


def name_checker(user_name):
    if models_user_exist(user_name):
        raise PowerBankUserException('该用户名已存在：{}'.format(user_name))


def user_exist(user_name):
    return models_user_exist(user_name)


def add_user(name, phone, password):
    return models_add_user(name, phone=phone, to_md5(password))


def load_user(name, instance4foreign_key=None):
    return models_load_user(name, instance4foreign_key)


def user_login_update(user_name):
    models_update_login(user_name)
