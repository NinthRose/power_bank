import threading

from boto.sdb.db import blob

from orca.common.exceptions.upload_download.file_exception import OrcaFileException
from orca.common.upload_download.file_operation import write_file
from orca.view_service.request_service import request_parser, param_int_checker, param_str_checker

_dict_rlock = threading.RLock()
with _dict_rlock:
    _chunk_dict = dict()


def __combination_chunks(chunk_dict, file_blob, user_id, file_id, filename, current_chunk, total_chunk):
    blob_lines = blob.Blob.read(file_blob)
    key = current_chunk
    dict_key = ':'.join([file_id, filename, user_id])
    if dict_key not in chunk_dict:
        chunk_dict[dict_key] = dict()
    chunk_dict[dict_key][key] = blob_lines
    if len(chunk_dict[dict_key]) == total_chunk:
        cup = bytearray()
        for i in range(total_chunk):
            cup += chunk_dict[dict_key][i]
        chunk_dict[dict_key] = cup
        return True
    else:
        return False


def request_uploader(request):
    args = ['filename', 'currChunk', 'totalChunk', 'fileId', 'dataSetName']
    filename, current_chunk, total_chunk, file_id, data_set_name = request_parser(request, args, is_post=True)
    file_id, data_set_name = param_str_checker([file_id, data_set_name], ['fileId', 'dataSetName'])
    current_chunk, total_chunk = param_int_checker([current_chunk, total_chunk], ['currChunk', 'totalChunk'])
    user_id = request.username
    file = request.FILES.getlist('file')
    if len(file) != 1:
        raise OrcaFileException('当前接口只接受单文件')
    file_blob = file[0]

    try:
        filename = filename.strip()
        assert filename
    except:
        filename = file_blob.name

    with _dict_rlock:
        dict_key = ':'.join([file_id, filename, user_id])
        combination = __combination_chunks(
            _chunk_dict, file_blob, user_id, file_id, filename, current_chunk, total_chunk)
        file_bytes = bytes(_chunk_dict.pop(dict_key)) if combination else None
        return write_file(request.username, data_set_name, filename, file_bytes)
