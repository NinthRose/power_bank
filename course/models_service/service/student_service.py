from course.models_service.models.models_object import model_lock, PD


def register_student(name, phone, comment):
    with model_lock:
        PD.register(name, phone, comment)


def update_student(phone, name, comment):
    with model_lock:
        student = PD.get_student(phone)
        student.update_info(name, comment)


def search_student(keyword, page_size, page_num):
    with model_lock:
        students = PD.search_students(keyword)
        page_students = students[(page_num - 1) * page_size:page_num * page_size]
        return len(students), [
            {'name': s.name, 'phone': s.phone, 'ctime': str(s.get_ctime())[:-7], 'utime': str(s.get_utime())[:-7],
             'all': s.all, 'rest': s.rest, 'comment': s.comment}
            for s in page_students]
