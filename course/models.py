from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    last_login = models.DateTimeField(null=True)
    ctime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
        ordering = ['-ctime']


class Session(models.Model):
    session = models.CharField(max_length=64, primary_key=True)
    user = models.CharField(max_length=64)
    mtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "session"
        ordering = ['-ctime']
