import datetime
import json

import os
from django.http import HttpResponse, StreamingHttpResponse

from course.common.constants.view_constants import StatusCode


def success_response(message, result=None):
    return create_response(StatusCode.SUCCESS, message, result)


def failed_response(message, result=None):
    return create_response(StatusCode.FAILURE, message, result)


def session_response(message, result=None):
    return create_response(StatusCode.TIMEOUT, message, result)


def special_response(message, result=None):
    return create_response(StatusCode.SPECIAL, message, result)


def create_response(state_code, message, result=None):
    res = {'statusCode': state_code, 'message': message}
    res['data'] = result
    return HttpResponse(json.dumps(res, ensure_ascii=False, indent=4))


def __file_iterator(file_path, chunk_size=512):
    if str(file_path).lower().endswith('.zip'):
        mode = 'rb'
    else:
        mode = 'r'
    with open(file_path, mode=mode) as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


def file_response(file_path, is_txt=None):
    if is_txt:
        response = StreamingHttpResponse(file_path)
        file_name = str(datetime.datetime.now()).replace(' ', '_')
    else:
        response = StreamingHttpResponse(__file_iterator(file_path))
        file_dir, file_name = os.path.split(file_path)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
    return response
