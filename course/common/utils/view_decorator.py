import functools
import json
import logging
import os
import traceback

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from course.common.constants.view_constants import RequestMethod, StatusCode
from course.common.exceptions.orca_exception import PowerBankException
from course.common.view_service.response_service import failed_response


def view_online(view_msg_prefix, request_method=None):
    if not request_method:
        request_method = RequestMethod.POST

    def _http_method_check(fn):

        def _wrapper(*args, **kwargs):
            for param in args:
                if isinstance(param, WSGIRequest):
                    if param.method == request_method:
                        pass
                    else:
                        res = {
                            'stateCode': StatusCode.WRONG_METHOD,
                            'message': u"请求方式错误"}
                        return HttpResponse(json.dumps(res, ensure_ascii=False))
            try:
                result = fn(*args, **kwargs)
                return result
            except PowerBankException as e:
                logging.debug(e)
                return failed_response(str(e))
            except Exception as e:
                FAILURE_MSG = "失败, {}"
                logging.error("%s%s, err-msg: %s, traceback: %s" % (
                    view_msg_prefix, FAILURE_MSG, e, traceback.format_exc()))
                return failed_response(
                    view_msg_prefix + FAILURE_MSG.format(e), result=None)

        return _wrapper

    return _http_method_check


view_checker = view_online


def log_pid(_func=None, *, func_name=None):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper_log(*args, **kwargs):
            f_name = func_name if func_name else func.__name__
            logging.debug('call %s in pid: %s' % (f_name, os.getpid()))
            return func(*args, **kwargs)

        return wrapper_log

    if _func is None:
        return decorator_log
    else:
        return decorator_log(_func)


def deprecated(msg=None):
    if msg is None:
        msg = u'当前接口已弃用。'

    def deprecated(fn):
        def wrapper(*args, **kwargs):
            # result = fn(*args, **kwargs)
            result = failed_response(msg)
            return result

        return wrapper

    return deprecated


def deprecating():
    return deprecated(u'当前接口尚未启用')
