import re

from course.common.configuration.config_parser import power_config
from course.common.exceptions.params.param_exception import PowerBankParamException
from course.common.utils.md5 import to_md5
from course.common.utils.view_decorator import view_checker
from course.common.view_service.request_service import request_parser, param_str_checker, param_int_checker
from course.common.view_service.response_service import failed_response, success_response
from course.models_service.service.session_service import add_session, remove_session
from course.models_service.service.user_service import add_user, user_exist, load_user, user_login_update, reset_user, \
    search_user


@view_checker('注册用户')
def create_account(request):
    args = ['key', 'name', 'password', 'phone', 'returnJson']
    key, name, password, phone, return_json = request_parser(request, args, is_post=True)
    key, name, password, phone = param_str_checker([key, name, password, phone], ['key', 'name', 'password', 'phone'],
                                                   [False, False, True, False])
    if not re.match('[0-9]{11,11}', phone):
        raise PowerBankParamException('手机号非法：{}'.format(phone))
    if not password:
        password = phone[-4:]
    password_md5 = power_config.get_config('config', 'PASSWORD', str)
    if to_md5(key) == password_md5:
        user = add_user(phone, name, password)
        return success_response('创建用户成功', {'user': user})
    else:
        return failed_response('密码错误！')


@view_checker('重置账户')
def reset_account(request):
    args = ['key', 'name', 'password', 'phone']
    key, name, password, phone = request_parser(request, args, is_post=True)
    key, name, password, phone = param_str_checker([key, name, password, phone],
                                                   ['key', 'name', 'password', 'phone'], [False, True, True, False])
    if not (name or password):
        raise PowerBankParamException('name和password不可都为空')
    if not name:
        name = None
    if not password:
        password = None
    password_md5 = power_config.get_config('config', 'PASSWORD', str)
    if to_md5(key) == password_md5:
        user = reset_user(phone, name, password)
        return success_response('重置用户信息成功', {'user': user})
    else:
        return failed_response('密码错误！')


@view_checker('登录')
def login(request):
    args = ['phone', 'password']
    phone, password = request_parser(request, args, is_post=True)
    phone, password = param_str_checker([phone, password], ['userId', 'password'])
    if not user_exist(phone):
        return failed_response(u"您未注册，请先注册")
    user = load_user(phone)
    if to_md5(password) != user['password']:
        return failed_response(u"登录失败，用户名或密码错误")
    print(u"用户{}已登录".format(phone))
    user_login_update(phone)
    session_id = add_session(phone)
    response = success_response('登录成功')
    response.set_cookie('phone', phone, expires=None)
    response.set_cookie('session', session_id, expires=None)
    return response


@view_checker('搜索账户')
def search(request):
    args = ['keyword', 'pageSize', 'pageNum']
    keyword, page_size, page_num = request_parser(request, args, is_post=True)
    page_size, page_num = param_int_checker([page_size, page_num], ['pageSize', 'pageNum'])
    users = search_user(keyword, page_size, page_num)
    return success_response('搜索用户完成', users)


@view_checker('登出')
def logout(request):
    session = request.COOKIES.get('session')
    request.COOKIES.clear()
    remove_session(session)
    return success_response('用户登出')


@view_checker('用户信息')
def info(request):
    return success_response('获取用户信息成功', request.user.to_dict())
