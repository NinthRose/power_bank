import functools
import json

from course.common.exceptions.params.param_exception import PowerBankParamException


def request_parser(request, args: list, is_get=None, is_post=None):
    try:
        assert len(args) > 0
        if is_get:
            get_val = request.GET.get
            vals = [get_val(arg) for arg in args]
        elif is_post and request.POST:
            get_val = request.POST.get
            vals = [get_val(arg) for arg in args]
        else:
            val_list = json.loads(request.body.decode())
            vals = list()
            for arg in args:
                vals.append(val_list[arg] if arg in val_list.keys() else None)
        return vals if len(vals) > 1 else vals[0]
    except:
        raise PowerBankParamException('参数缺省：{}'.format(args))


def params_supporter():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            if not isinstance(args[0], list):
                return func(*args)
            length = None
            for ps in args:
                if length is None:
                    length = len(ps)
                    continue
                assert length == len(ps), 'illegal params:the different length params.'
            params = list()
            for ps in zip(*args):
                params.append(func(*ps))
            return params

        return wrapper

    return decorator


@params_supporter()
def param_str_checker(p, name):
    if isinstance(p, int):
        return p
    try:
        p = p.strip()
        assert p
        return p
    except:
        raise PowerBankParamException('{}参数有误：{}'.format(name, p))


@params_supporter()
def param_int_checker(p, name):
    try:
        return int(p)
    except:
        raise PowerBankParamException('{}参数有误：{}'.format(name, p))


@params_supporter()
def param_bool_checker(p, name, default):
    if p is None:
        p = default
    elif isinstance(p, str):
        if p.lower() == 'true':
            p = True
        elif p.lower() == 'false':
            p = False
        else:
            raise PowerBankParamException('{}参数有误:{}'.format(name, p))
    elif isinstance(p, bool):
        pass
    else:
        raise PowerBankParamException('{}参数有误:{}'.format(name, p))
    return p


def param_json_checker(p, name):
    if p is not None and not isinstance(p, str):
        return p
    try:
        return json.loads(p)
    except:
        raise PowerBankParamException('{}参数有误,expect json but:{}'.format(name, p))
