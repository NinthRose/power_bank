"""power_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.shortcuts import render
from django.views.static import serve

from course.views import account_views
from power_bank.settings import STATIC_ROOT


class PowerBankUrl():
    def __init__(self, orca_prefix=None):
        if orca_prefix is None:
            orca_prefix = r'^powerBank/{}'

        admin_url = orca_prefix.format('admin/{}')
        user_url = orca_prefix.format('user/{}')

        self.admin_url = admin_url
        self.user_url = user_url


pbu = PowerBankUrl()


def index(request):
    return render(request, "index.html")


urlpatterns = [

    url(pbu.admin_url.format('account/create'), account_views.create_account),

    url(pbu.user_url.format('account/login'), account_views.login),
    url(pbu.user_url.format('account/logout'), account_views.logout),
    url(pbu.user_url.format('account/info'), account_views.info),
    url(r'^$', index),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]
