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
    args = ['password', 'account', 'accountPassword', 'phone', 'returnJson']
    password, account, account_password, phone, return_json = request_parser(request, args, is_post=True)
    password, account, account_password, phone = param_str_checker([password, account, account_password, phone],
                                                                   ['password', 'account', 'accountPassword', 'phone'])
    return_json = param_bool_checker(return_json, 'returnJson', False)
    if to_md5(password) == 'cf6e6f5a3c76dc910a7d8b0f98462b68':
        user = add_user(account, phone, account_password)
        if return_json:
            return success_response('创建用户成功', {'user': user})
        else:
            return HttpResponse('<title>创建用户</title><h3>用户名为：{}，密码为：{}</h3><p><form action="/">'
                                '<input type="submit" value="返回"></form></p>'.format(account, account_password))
    else:
        return HttpResponse('密码错误！')


@view_checker('登录')
def login(request):
    args = ['userId', 'password']
    user_id, password = request_parser(request, args, is_post=True)
    user_id, password = param_str_checker([user_id, password], ['userId', 'password'])
    if not user_exist(user_id):
        return failed_response(u"您未注册，请先注册")
    user = load_user(user_id)
    if not user['activation']:
        return failed_response(u"账号还未激活，请前往邮箱({})激活账号！".format(user['email']))
    if to_md5(password) != user['password']:
        return failed_response(u"登录失败，用户名或密码错误")
    logging.info(u"用户{}已登录".format(user_id))
    user_login_update(user_id)
    session_id = add_session(user_id)
    response = success_response('登录成功')
    response.set_cookie('user', user_id, expires=None)
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
