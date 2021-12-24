import datetime
import time


class MyClock(object):

    def __init__(self):
        super().__init__()
        self.cclock = time.time()
        self.uclock = time.time()
        self.session = None

    def update(self):
        self.uclock = time.time()

    def get_ctime(self):
        return str(datetime.datetime.fromtimestamp(self.cclock))[:-7]

    def get_utime(self):
        return str(datetime.datetime.fromtimestamp(self.uclock))[:-7]


class Lesson(MyClock):
    def __init__(self, phone, lesson_type):
        super().__init__()
        self.lesson_type = lesson_type
        self.phone = phone
        self.conduct = False
        self.refund = False

    def get_lesson_type(self):
        return self.lesson_type


LESSON_TYPES = ["personal", "lesson", "free"]


class Student(MyClock):
    def __init__(self, name, phone, comment=None):
        super().__init__()
        self.name = name if name else phone[-4:0]
        self.phone = phone
        self.comment = comment
        self.lessons = list()
        self.all = [0] * len(LESSON_TYPES)
        self.rest = [0] * len(LESSON_TYPES)

    def get_name(self):
        return self.name

    def update_info(self, name, comment):
        if name:
            self.name = name
        if comment:
            self.comment = comment

    def type_index(self, lesson_type):
        if lesson_type not in LESSON_TYPES:
            raise Exception("课程类型不支持：{} not in {}", lesson_type, LESSON_TYPES)
        return LESSON_TYPES.index(lesson_type)

    def add_lesson(self, num, lesson_type):
        if num <= 0:
            return False
        index = self.type_index(lesson_type)
        for i in range(num):
            self.lessons.append(Lesson(self.phone, lesson_type))
        self.all[index] += num
        self.rest[index] += num
        return True

    def conduct(self, num, lesson_type):
        index = self.type_index(lesson_type)
        if num > self.rest[index] or num <= 0:
            raise Exception("没有可消费课程: rest {} lessons, conduct {}".format(self.rest[index], num))
        self.operate(num, lesson_type, conduct=True)
        self.rest[index] -= num

    def refund(self, num, lesson_type):
        index = self.type_index(lesson_type)
        if num > self.rest[index] or num <= 0:
            raise Exception("没有可退课程: rest {} lessons, refund {}".format(self.rest[index], num))
        self.operate(num, lesson_type, recover=True)
        self.all[index] -= num
        self.rest[index] -= num

    def operate(self, num, lesson_type, conduct=None, recover=None):
        for lesson in self.lessons:
            if num == 0:
                return
            if lesson_type != lesson.get_lesson_type():
                continue
            if not lesson.conduct and not lesson.refund:
                if conduct:
                    lesson.conduct = True
                if recover:
                    lesson.refund = True
                lesson.update()
                self.update()
                num -= 1
        if num != 0:
            raise Exception("操作课程有误")


class PowerData(MyClock):

    def __init__(self):
        super().__init__()
        self.students = dict()

    def exist(self, phone):
        return phone in self.students.keys()

    def register(self, name, phone, comment):
        if self.exist(phone):
            raise Exception("{} registered".format(phone))
        student = Student(name, phone, comment)
        student.id = len(self.students) + 1
        self.students[phone] = student

    def get_student(self, phone) -> Student:
        try:
            return self.students[phone]
        except KeyError:
            phone = int(phone)
            for p, s in self.students.items():
                if s.id == phone:
                    return s
            raise Exception("{} not exists.".format(phone))

    def search_students(self, keyword):
        phones = self.students.keys()
        if keyword:
            phones = [p for p in phones if keyword in p or keyword in self.students.get(p).get_name()]
        res = [self.students.get(p) for p in phones]
        res.reverse()
        return res

    def update_session(self):
        self.session = time.time()
        return self.session

    def get_session(self, timeout):
        if self.session is None or time.time() - self.session > timeout:
            self.session = None
        return self.session

    def clear_session(self):
        self.session = None
