from course.common.configuration.config_parser import power_config
from course.common.utils.md5 import to_md5
from course.common.utils.view_decorator import view_checker
from course.common.view_service.request_service import request_parser, param_str_checker
from course.common.view_service.response_service import failed_response, success_response


@view_checker('登录')
def login(request):
    args = ['password']
    password = request_parser(request, args, is_post=True)
    password = param_str_checker(password, args)
    if to_md5(password) != power_config.get_config('config', 'PASSWORD', str):
        return failed_response(u"登录失败，密码错误")
    try:
        session_id = add_session()
    except Exception:
        session_id = None

    response = success_response('登录成功')
    response.set_cookie('session', session_id, expires=None)
    return response


@view_checker('登出')
def logout(request):
    session = request.COOKIES.get('session')
    request.COOKIES.clear()
    if not session:
        remove_session(session)
    return success_response('用户登出')
