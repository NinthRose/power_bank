from datetime import datetime

from course.models_service.constants.models import models_constant
from course.models_service.models.source import models_add_source, models_count_source, models_info_source, \
    models_consume_source
from course.models_service.models.user import models_load_user


def add_source(user, num):
    if models_constant.is_id(user):
        user = models_load_user(user, instance4foreign_key=True)
    models_add_source(user, num)


def statistic_source(user, page_size, page_num):
    if models_constant.is_id(user):
        user = models_load_user(user, instance4foreign_key=True)
    total = models_count_source(user)
    used = models_count_source(user, True)
    last = models_count_source(user, False)
    info = models_info_source(user, page_size, page_num)
    for i in info:
        for k, v in i.items():
            if isinstance(v, datetime):
                i[k] = str(v)
    return {'total': total, 'used': used, 'last': last, 'sources': info}


def consume_source(user, num):
    if models_constant.is_id(user):
        user = models_load_user(user, instance4foreign_key=True)
    assert models_count_source(user, False) >= num, '剩余课程不足'
    models_consume_source(user, num)
