#coding=utf-8
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)  # 用户名
    upwd = models.CharField(max_length=40)   # 密码
    uemail = models.CharField(max_length=20)  # 邮箱
    ushou = models.CharField(max_length=10)  # 收
    uphone = models.CharField(max_length=20)  # 手机号
    udizhi = models.CharField(max_length=100)  # 地址
    uyoubian = models.CharField(max_length=6)  # 邮编


