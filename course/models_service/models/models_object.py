import json
import os
import threading
import time

from course.models_service.models.models import PowerData, Lesson, Student
from data import data_dir

JSON_SUFFIX = ".json"

PD = PowerData()


def dict2power(d):
    key_students = 'students'
    key_lessons = 'lessons'
    if key_students in d:
        PD.__dict__.update(d)
        return PD
    # student
    if key_lessons in d:
        s = Student(d['name'], d['phone'])
        s.__dict__.update(d)
        lessons = d.pop(key_lessons)
        s.lessons = list()
        for lesson in lessons:
            l = Lesson(d['phone'])
            l.__dict__.update(lesson)
            s.lessons.append(l)
        return s
    return d


def get_latest():
    max = None
    latest_file = None
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith(JSON_SUFFIX):
                clock = float(file.replace(JSON_SUFFIX, ""))
                if max is None or clock > max:
                    max = clock
                    latest_file = file
    if latest_file is None:
        return PD
    with open(os.path.join(data_dir, latest_file)) as input:
        return json.load(input, object_hook=dict2power)


def dumps(obj):
    now = str(time.time())
    json_path = os.path.join(data_dir, now + JSON_SUFFIX)
    with open(json_path, 'w') as output:
        json.dump(obj, output, default=lambda obj: obj.__dict__, ensure_ascii=False)


def dumps2json(obj):
    return json.dumps(obj, default=lambda obj: obj.__dict__, ensure_ascii=False)


def dumps2basic(obj):
    return json.loads(json.dumps(obj, default=lambda obj: obj.__dict__, ensure_ascii=False))


model_lock = threading.RLock()
get_latest()

# # test
# latest = get_latest()
# print(latest)
# pd = PowerData()
# print(pd.get_ctime())
# name = 'name1'
# phone = '15313135514'
# pd.register(name, phone)
# pd.get(phone).add_lesson(5)
# pd.get(phone).conduct(2)
# pd.get(phone).recover(2)
# dumps(pd)
