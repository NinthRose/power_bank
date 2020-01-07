class RequestMethod:
    POST = "POST"
    GET = "GET"


class StatusCode:
    FAILURE = 300
    EXCEPTION = 250
    SUCCESS = 200
    WRONG_METHOD = 406
    SPECIAL = 301
    FORBIDDEN = 403
    # 自定义207为任务完成状态码
    CONSUMMATION = 207
    # Session 超时返回的状态码
    TIMEOUT = 208
    # 资源创建或修改成功, 因前端框架对非200的状态码统一拦截弹红色警示框, 因此, 将此状态码的值由201改为200
    CREATED = 200
    # 请求参数错误
    BADREQUEST = 400
    # 资源已存在, 比如用户名已存在
    CONFLICT = 409
    # 执行成功, 不返回任务值, 因前端框架对非200的状态码统一拦截弹红色警示框, 因此, 将此状态码的值由204改为200
    EXECUTION_SUCCEED = 200
