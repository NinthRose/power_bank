from django.utils.deprecation import MiddlewareMixin

from course.common.view_service.response_service import session_response


class SessionMiddleware(MiddlewareMixin):
    """
    MiddlewareMixin 为继承过来的函数，该函数中有两个方法:
    __init__  该方法在项目启动时执行一次，以后在不执行，用于初始化一下信息
    __call__  该方法在浏览器发起请求时执行，方法里有调用process_request和process_response的代码逻辑
    **************如果不继承MiddlewareMixin方法，就需要自己实现__init__和__call__方法，不然会报错**************
    """

    def __init__(self, get_response=None):
        MiddlewareMixin.__init__(self, get_response)

        urls_ignore_prefix = list()
        urls_ignore_prefix.append('static')
        urls_ignore_prefix.append('templates')
        self.urls_ignore_prefix = urls_ignore_prefix

    def process_request(self, request):
        path = request.path
        # access_token = request.META.get('HTTP_PRIVATE_TOKEN', None)
        if self.is_ignore_url(path):
            pass
        else:
            session = request.COOKIES.get('session')
            if not session:
                return session_response("账号未登录,请立即登录")
            if is_illegal_session(session):
                response = session_response("登录异常,请重新登录")
                response.cookies.clear()
                return response

        return None

    def process_response(self, request, response):
        return response

    def process_exception(self, response, exception):
        raise Exception('session middleware failed.')

    def is_ignore_url(self, url):
        url = url.lstrip('/')
        if not url or url == 'index.html':
            return True
        if url.endswith("login") or url.endswith("logout"):
            return True
        for ignore_start in self.urls_ignore_prefix:
            if str(url).startswith(ignore_start):
                return True
        return False
