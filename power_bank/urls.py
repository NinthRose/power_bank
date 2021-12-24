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

from course.views import account_views, lesson_views, student_views
from power_bank.settings import STATIC_ROOT


class PowerBankUrl(object):
    def __init__(self, power_prefix=None):
        if power_prefix is None:
            power_prefix = r'^powerBank/{}'

        self.admin_url = power_prefix
        self.student_url = power_prefix.format('student/{}')
        self.lesson_url = power_prefix.format('lesson/{}')


pbu = PowerBankUrl()


def index(request):
    return render(request, "index.html")


urlpatterns = [

    url(pbu.admin_url.format('login'), account_views.login),
    url(pbu.admin_url.format('logout'), account_views.logout),

    url(pbu.student_url.format('register'), student_views.register),
    url(pbu.student_url.format('update'), student_views.update),
    url(pbu.student_url.format('search'), student_views.search),

    url(pbu.lesson_url.format('add'), lesson_views.add),
    url(pbu.lesson_url.format('update'), lesson_views.update),
    url(pbu.lesson_url.format('search'), lesson_views.search),

    url(r'^$', index),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

]
