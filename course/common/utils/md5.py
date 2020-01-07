import hashlib


def to_md5(string):
    h = hashlib.md5()
    h.update(string.encode('utf-8'))
    return h.hexdigest()
