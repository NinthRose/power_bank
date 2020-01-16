from course.common.exceptions.models.user_exception import PowerBankUserException
from course.common.utils.md5 import to_md5
from course.models_service.models.user import models_user_exist, models_add_user, models_load_user, models_update_login, \
    models_reset_user, models_search_user, models_page_user


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


def search_user(keyword, page_size, page_num):
    return {'page': models_search_user(keyword, page_size, page_num), 'total': models_page_user(keyword, page_num)}


def user_login_update(phone):
    models_update_login(phone)
