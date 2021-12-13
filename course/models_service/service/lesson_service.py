from course.models_service.models.models_object import model_lock, PD


def add_lesson(phone, num):
    with model_lock:
        user = PD.get_student(phone)
        user.add_lesson(num)


def update_lesson(phone, num, conduct=None, refund=None):
    with model_lock:
        user = PD.get_student(phone)
        if conduct:
            user.conduct(num)
        elif refund:
            user.refund(num)
