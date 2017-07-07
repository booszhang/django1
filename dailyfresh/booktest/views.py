# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse
from models import *
from hashlib import sha1
from datetime import time


# Create your views here.

def register(request):
    context = {'title': '注册'}

    return render(request, 'booktest/register.html', context)


def login(request):
    context = {'title': '登录'}

    return render(request, 'booktest/login.html', context)


def register_handle(request):
    # 接受数据
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    uemail = post.get('user_email')
    # 加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    # 在数据库创建对象
    user = UserInfo()
    user.uname= uname
    user.upwd= upwd_sha1
    user.uemail= uemail

    # 保存
    user.save()

    # 保存返回到登录页面
    return redirect('/login/')


# 查看数据库名字是否存在
def register_hies(request):

    uname = request.GET.get('uname')

    reseng = UserInfo.objects.filter(uname=uname).count() # count　是否存在

    context = {'hies': reseng}

    return JsonResponse(context)

# 查看密码是否跟数据库一致
def login_pwd(request):
    upwd = request.POST.get('upwd')

    reseng = UserInfo.objects.filter(upwd=upwd).count() # count  检测是否存在

    context = {'hies': reseng}

    return JsonResponse(context)


# 浏览器cookie记住
def cookie_jizi(request):
    uname = request.COOKIES.get('uname')

    context = {'title': '登录', 'uname': 'uname'}
    return render(request, 'login.html', context)

# # 记住用户名
# def cookie_yhm(request):
#     # 首先想的是记住用户　记住的是什么？账号和密码
#     # 获取录入的账号和密码
#     post = request.POST
#     uname = post.username
#     upwd = post.pwd
#     uname_jz = post.get('cook_yhm')
#
#     s1 = sha1()
#     s1.update(upwd)
#     s1_upwd = s1.hexdigest()
#
#     #对密码加密
#
#     context = {'title': '登录', 'uname': 'uname', 'upwd': 'upwd'}
#
#     users = UserInfo.objects.filter(uname=uname)
#     if len(users)==0:
#         context[]
#
#         # 提示用户名错误





























