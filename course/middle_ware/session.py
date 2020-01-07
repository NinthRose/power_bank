import logging

from django.utils.deprecation import MiddlewareMixin

from course.common.view_service.response_service import session_response
from course.models_service.service.session_service import is_illegal_session
from course.models_service.service.user_service import load_user
from power_bank.urls import PowerBankUrl


class SessionMiddleware(MiddlewareMixin, PowerBankUrl):
    """
    MiddlewareMixin 为继承过来的函数，该函数中有两个方法:
    __init__  该方法在项目启动时执行一次，以后在不执行，用于初始化一下信息
    __call__  该方法在浏览器发起请求时执行，方法里有调用process_request和process_response的代码逻辑
    **************如果不继承MiddlewareMixin方法，就需要自己实现__init__和__call__方法，不然会报错**************
    """

    def __init__(self, get_response=None):
        MiddlewareMixin.__init__(self, get_response)
        PowerBankUrl.__init__(self, 'powerBank/{}')
        urls_ignore = list()
        urls_ignore.append(self.admin_url.format('account/create'))
        urls_ignore.append(self.user_url.format('account/register'))
        urls_ignore.append(self.user_url.format('account/login'))
        self.urls_ignore = urls_ignore

        urls_ignore_prefix = list()
        urls_ignore_prefix.append('orca/test')
        self.urls_ignore_prefix = urls_ignore_prefix

    def process_request(self, request):
        path = request.path
        # access_token = request.META.get('HTTP_PRIVATE_TOKEN', None)
        if self.is_ignore_url(path):
            pass
        else:
            session = request.COOKIES.get('session')
            user = request.COOKIES.get('user')
            if not session or not user:
                return session_response("账号未登录,请立即登录")
            if is_illegal_session(session):
                logging.warning(f"用户{user}下线")
                response = session_response("登录异常,请重新登录")
                response.cookies.clear()
                return response

            request.username = user
            request.user = load_user(user, True)

        return None

    def process_response(self, request, response):
        return response

    def process_exception(self, response, exception):
        raise Exception('session middleware failed.')

    def is_ignore_url(self, url):
        url = url.lstrip('/')
        if not url or url == 'index.html':
            return True
        if url in self.urls_ignore:
            return True
        for ignore_start in self.urls_ignore_prefix:
            if str(url).startswith(ignore_start):
                return True
        return False
