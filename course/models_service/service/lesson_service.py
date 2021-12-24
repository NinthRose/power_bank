from course.models_service.models.models_object import model_lock, PD

LESSON_MAP = {"personal": "私教课", "lesson": "正课", "free": "复习课"}


def transform_lesson(lt):
    try:
        return LESSON_MAP[lt]
    except KeyError:
        return lt


def add_lesson(phone, num, lesson_type):
    with model_lock:
        user = PD.get_student(phone)
        return user.add_lesson(num, lesson_type)


def update_lesson(phone, num, lesson_type, conduct=None, refund=None):
    with model_lock:
        user = PD.get_student(phone)
        if conduct:
            user.conduct(num, lesson_type)
        elif refund:
            user.refund(num, lesson_type)


def search_lesson(phone, size, num):
    with model_lock:
        user = PD.get_student(phone)
        start = -size * num
        end = start + size
        if 0 <= end:
            lessons = user.lessons[start:]
        else:
            lessons = user.lessons[start:end]
        lessons.reverse()
        return len(user.lessons), user.rest, [{
            "date": l.get_ctime(),
            "conduct": l.get_utime() if l.conduct else "否",
            "refund": l.get_utime() if l.refund else "否",
            "type": transform_lesson(l.get_lesson_type())
        } for l in lessons]
