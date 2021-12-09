from datetime import datetime
from django.db import models

#
# class Student(models.Model):
#     phone = models.CharField(max_length=16, primary_key=True)
#     name = models.CharField(max_length=32)
#     ctime = models.DateTimeField(auto_now_add=True)
#     utime = models.DateTimeField(null=True)
#
#     class Meta:
#         db_table = 'user'
#         ordering = ['-ctime']
#
#     def to_dict(self):
#         user_dict = self.__dict__.copy()
#         if '_state' in user_dict:
#             user_dict.pop('_state')
#         for key, value in user_dict.items():
#             if isinstance(value, datetime):
#                 user_dict[key] = str(value)
#         return user_dict
#
#
# class Session(models.Model):
#     session = models.CharField(max_length=64, primary_key=True)
#     mtime = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'session'
#
#
# class Lesson(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='user')
#     ctime = models.DateTimeField(auto_now_add=True)
#     conduct = models.BooleanField(default=False)
#     recover = models.BooleanField(default=False)
#     utime = models.DateTimeField(null=True)
