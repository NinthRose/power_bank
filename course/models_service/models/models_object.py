import json
import os
import threading
import time

from course.models_service.models.models import PowerData
from data import data_dir

JSON_SUFFIX = ".json"


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
    pd = PowerData()
    if latest_file is None:
        return pd
    with open(os.path.join(data_dir, latest_file)) as input:
        pd.__dict__.update(json.load(input))
        return pd


def dumps(obj):
    now = str(time.time())
    json_path = os.path.join(data_dir, now + JSON_SUFFIX)
    with open(json_path, 'w') as output:
        json.dump(obj, output, default=lambda obj: obj.__dict__, ensure_ascii=False)


model_lock = threading.RLock()
pd = get_latest()

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
