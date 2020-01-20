from course.common.configuration.config_parser import power_config
from course.common.utils.md5 import to_md5
from course.common.utils.view_decorator import view_checker
from course.common.view_service.request_service import request_parser, param_int_checker, param_str_checker
from course.common.view_service.response_service import success_response, failed_response
from course.models_service.service.source_service import add_source, statistic_source, consume_source


@view_checker('充值课程')
def add(request):
    args = ['password', 'phone', 'num']
    password, phone, num = request_parser(request, args, is_post=True)
    password_md5 = power_config.get_config('config', 'PASSWORD', str)
    num = param_int_checker(num, 'num')
    password, phone = param_str_checker([password, phone], ['password', 'phone'])
    if to_md5(password) != password_md5:
        return failed_response('密码错误')
    add_source(phone, num)
    return success_response('充值课程成功', )


@view_checker('消费课程')
def consume(request):
    args = ['password', 'phone', 'num']
    password, phone, num = request_parser(request, args, is_post=True)
    password_md5 = power_config.get_config('config', 'PASSWORD', str)
    num = param_int_checker(num, 'num')
    password, phone = param_str_checker([password, phone], ['password', 'phone'])
    if to_md5(password) != password_md5:
        return failed_response('密码错误')
    consume_source(phone, num)
    return success_response('消费课程成功')


@view_checker('统计课程信息')
def statistic(request):
    args = ['phone', 'pageNum', 'pageSize']
    phone, page_num, page_size = request_parser(request, args, is_post=True)
    page_num, page_size = param_int_checker([page_num, page_size], ['pageNum', 'pageSize'])
    phone = param_str_checker(phone, 'phone')
    return success_response('统计课程信息成功', statistic_source(phone, page_size, page_num))
