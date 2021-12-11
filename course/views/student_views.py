import re

from course.common.exceptions.params.param_exception import PowerBankParamException
from course.common.utils.view_decorator import view_checker
from course.common.view_service.request_service import request_parser, param_str_checker, param_int_checker
from course.common.view_service.response_service import success_response, failed_response
from course.models_service.service.student_service import register_student, search_student


@view_checker('注册用户')
def register(request):
    args = ['name', 'phone']
    name, phone = request_parser(request, args, is_post=True)
    name, phone = param_str_checker([name, phone], args)
    if not re.match('[0-9]{11,11}', phone):
        raise PowerBankParamException('手机号非法：{}'.format(phone))
    if not name:
        name = phone[-4:]

    user = register_student(name, phone)
    return success_response('创建用户成功', {'user': user})


@view_checker('重置账户')
def update(request):
    args = ['name', 'phone']
    name, phone = request_parser(request, args, is_post=True)
    name, phone = param_str_checker([name, phone], args)
    user = reset_student(phone, name)
    return success_response('重置用户信息成功', {'user': user})


@view_checker('搜索账户')
def search(request):
    args = ['keyword', 'pageSize', 'pageNum']
    keyword, page_size, page_num = request_parser(request, args, is_post=True)
    page_size, page_num = param_int_checker([page_size, page_num], ['pageSize', 'pageNum'])
    users = search_student(keyword, page_size, page_num)
    return success_response('搜索用户完成', users)
