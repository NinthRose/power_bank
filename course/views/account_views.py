import logging

from django.http import HttpResponse
from django.shortcuts import render

from course.common.constants.view_constants import RequestMethod
from course.common.utils.md5 import to_md5
from course.common.utils.view_decorator import view_checker
from course.common.view_service.request_service import request_parser, param_str_checker, param_bool_checker
from course.common.view_service.response_service import failed_response, success_response
from course.models_service.service.session_service import add_session, remove_session
from course.models_service.service.user_service import add_user, user_exist, load_user, user_login_update


@view_checker('注册用户')
def create_account(request):
    args = ['key', 'name', 'password', 'phone', 'returnJson']
    key, name, password, phone, return_json = request_parser(request, args, is_post=True)
    key, name, password, phone = param_str_checker([key, name, password, phone],
                                                   ['key', 'name', 'password', 'phone'])
    return_json = param_bool_checker(return_json, 'returnJson', False)
    # if to_md5(password) == '7301aae0410ec3e3d7182451f8d84eb4':
    if to_md5(key) == '1f233f9859a982b42034dd17a45f264e':
        user = add_user(name, phone, password)
        return success_response('创建用户成功', {'user': user})
    else:
        return HttpResponse('密码错误！')


@view_checker('登录')
def login(request):
    args = ['phone', 'password']
    phone, password = request_parser(request, args, is_post=True)
    phone, password = param_str_checker([phone, password], ['userId', 'password'])
    if not user_exist(phone):
        return failed_response(u"您未注册，请先注册")
    user = load_user(phone)
    if not user['activation']:
        return failed_response(u"账号还未激活，请前往邮箱({})激活账号！".format(user['email']))
    if to_md5(password) != user['password']:
        return failed_response(u"登录失败，用户名或密码错误")
    logging.info(u"用户{}已登录".format(phone))
    user_login_update(phone)
    session_id = add_session(phone)
    response = success_response('登录成功')
    response.set_cookie('phone', phone, expires=None)
    response.set_cookie('session', session_id, expires=None)
    return response


@view_checker('登出', RequestMethod.GET)
def logout(request):
    session = request.COOKIES.get('session')
    request.COOKIES.clear()
    remove_session(session)
    response = render(request, 'index.html')
    response.cookies.clear()
    return response


@view_checker('用户信息')
def info(request):
    return success_response('获取用户信息成功', request.user.to_dict())
