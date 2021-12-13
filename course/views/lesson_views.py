from course.common.utils.view_decorator import view_checker
from course.common.view_service.request_service import request_parser, param_int_checker, param_str_checker
from course.common.view_service.response_service import success_response
from course.models_service.service.lesson_service import add_lesson, update_lesson


@view_checker('充值课程')
def add(request):
    args = ['phone', 'num']
    phone, num = request_parser(request, args, is_post=True)
    num = param_int_checker(num, 'num')
    phone = param_str_checker(phone, 'phone')
    add_lesson(phone, num)
    return success_response('充值课程成功', )


@view_checker('操作课程')
def update(request):
    args = ['phone', 'num', 'refund']
    phone, num, refund = request_parser(request, args, is_post=True)
    phone = param_str_checker(phone, args[0])
    num = param_int_checker(num, args[1])
    if not isinstance(refund, bool):
        raise Exception("类型有误")
    update_lesson(phone, num, not refund, refund)
    operate = "退" if refund else "划"
    return success_response('{}课成功'.format(operate))
