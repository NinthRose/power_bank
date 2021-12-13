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
        return datetime.datetime.fromtimestamp(self.cclock)

    def get_utime(self):
        return datetime.datetime.fromtimestamp(self.uclock)


class Lesson(MyClock):
    def __init__(self, phone):
        super().__init__()
        self.phone = phone
        self.conduct = False
        self.refund = False


class Student(MyClock):
    def __init__(self, name, phone):
        super().__init__()
        self.name = name if name else phone[-4:0]
        self.phone = phone
        self.lessons = list()
        self.all = 0
        self.rest = 0

    def add_lesson(self, num):
        if num <= 0:
            return
        for i in range(num):
            self.lessons.append(Lesson(self.phone))
        self.all += num
        self.rest += num

    def conduct(self, num):
        if num > self.rest or num <= 0:
            raise Exception("没有可消费课程: rest {} lessons, conduct {}".format(self.rest, num))
        self.rest -= num
        self.operate(num, conduct=True)

    def refund(self, num):
        if num > self.rest or num <= 0:
            raise Exception("没有可退课程: rest {} lessons, refund {}".format(self.rest, num))
        self.all -= num
        self.rest -= num
        self.operate(num, recover=True)

    def operate(self, num, conduct=None, recover=None):
        for lesson in self.lessons:
            if num == 0:
                return
            if not lesson.conduct and not lesson.refund:
                if conduct:
                    lesson.conduct = True
                if recover:
                    lesson.refund = True
                num -= 1


class PowerData(MyClock):

    def __init__(self):
        super().__init__()
        self.students = dict()

    def exist(self, phone):
        return phone in self.students.keys()

    def register(self, name, phone):
        if self.exist(phone):
            raise Exception("{} registered".format(phone))
        self.students[phone] = Student(name, phone)

    def get_student(self, phone) -> Student:
        try:
            return self.students[phone]
        except KeyError:
            raise Exception("{} not exists.".format(phone))

    def search_students(self, keyword):
        phones = self.students.keys()
        if keyword:
            phones = [p for p in phones if keyword in p]
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
