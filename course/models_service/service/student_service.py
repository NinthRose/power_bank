from course.models_service.models.models_object import model_lock, PD


def register_student(name, phone):
    with model_lock:
        PD.register(name, phone)


def search_student(keyword, page_size, page_num):
    with model_lock:
        students = PD.search_students(keyword)
        page_students = students[(page_num - 1) * page_size:page_num * page_size]
        return [{'name': s.name, 'phone': s.phone, 'ctime': str(s.get_ctime()), 'utime': str(s.get_utime())}
                for s in page_students]
