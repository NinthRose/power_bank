import datetime

from course.models import Source
from course.models_service.models_controller import models_lock


def models_add_source(user, num):
    with models_lock:
        for i in range(num):
            Source.objects.create(user=user)


def models_count_source(user, consume=None):
    with models_lock:
        sources = Source.objects.filter(user=user)
        if consume is not None:
            sources = sources.filter(consume=consume)
        return sources.count()


def models_info_source(user, page_size, page_num):
    start = (page_num - 1) * page_size
    end = page_num * page_size
    with models_lock:
        return list(Source.objects.filter(user=user)[start:end].values('ctime', 'stime'))


def models_consume_source(user, num):
    with models_lock:
        ss = Source.objects.filter(user=user, consume=False)[:num]
        for s in ss:
            s.consume = True
            s.stime = datetime.datetime.now()
            s.save()
