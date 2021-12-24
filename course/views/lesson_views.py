from course.common.utils.view_decorator import view_checker
from course.common.view_service.request_service import request_parser, param_int_checker, param_str_checker
from course.common.view_service.response_service import success_response, failed_response
from course.models_service.service.lesson_service import add_lesson, update_lesson, search_lesson


@view_checker('充值课程')
def add(request):
    args = ['phone', 'num', 'type']
    phone, num, lesson_type = request_parser(request, args, is_post=True)
    num = param_int_checker(num, 'num')
    phone, lesson_type = param_str_checker([phone, lesson_type], ["手机号码", "课程类型"])
    succeed = add_lesson(phone, num, lesson_type)
    if succeed:
        return success_response('充值课程成功')
    else:
        return failed_response("充值失败,数量或类型有误")


@view_checker('操作课程')
def update(request):
    args = ['phone', 'num', 'refund', 'type']
    phone, num, refund, lesson_type = request_parser(request, args, is_post=True)
    phone, lesson_type = param_str_checker([phone, lesson_type], ["手机号码", "课程类型"])
    num = param_int_checker(num, "课程数量")
    if not isinstance(refund, bool):
        raise Exception("类型有误")
    update_lesson(phone, num, lesson_type, not refund, refund)
    operate = "退" if refund else "划"
    return success_response('{}课成功'.format(operate))


@view_checker('查看账单')
def search(request):
    args = ['phone', 'pageSize', 'pageNum']
    phone, size, num = request_parser(request, args, is_post=True)
    phone = param_str_checker(phone, args.pop(0))
    size, num = param_int_checker([size, num], args)
    l_num, rest, lessons = search_lesson(phone, size, num)
    return success_response("查看账单", {"num": l_num, "rest": rest, "lessons": lessons})
