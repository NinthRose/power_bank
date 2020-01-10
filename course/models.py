from datetime import datetime
from django.db import models


class User(models.Model):
    phone = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=16)
    last_login = models.DateTimeField(null=True)
    ctime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
        ordering = ['-ctime']

    def to_dict(self, with_password=None):
        user_dict = self.__dict__.copy()
        if '_state' in user_dict:
            user_dict.pop('_state')
        for key, value in user_dict.items():
            if isinstance(value, datetime):
                user_dict[key] = str(value)
        if not with_password:
            user_dict.pop('password')
        return user_dict


class Session(models.Model):
    session = models.CharField(max_length=64, primary_key=True)
    user = models.CharField(max_length=64)
    mtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'session'
