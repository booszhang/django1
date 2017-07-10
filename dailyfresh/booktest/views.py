# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse
from models import *
from hashlib import sha1
import datetime
from zhuangshiqi import *


# Create your views here.

def register(request):
    context = {'title': '注册', 'top': '0'}

    return render(request, 'booktest/register.html', context)


def register_handle(request):
    # 接受数据
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    uemail = post.get('user_email')
    print uname
    print upwd
    print 1111
    # 加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()


    # 在数据库创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd= upwd_sha1
    user.uemail= uemail


    # 保存
    user.save()

    # 保存返回到登录页面
    return redirect('/login/')


def register_hies(request):

    uname = request.GET.get('uname')

    reseng = UserInfo.objects.filter(uname=uname).count()  # count　是否存在

    context = {'hies': reseng}

    return JsonResponse(context)


def login(request):
    if request.session.has_key('uid'):
        print 55555
        return redirect('/site/')
    print 44444
    uname = request.COOKIES.get('uname', '')  # 这个问题　为什么cookies没有记录

    context = {'title': '登录', 'uname': uname,  'top': '0'}

    return render(request, 'booktest/login.html', context)

def login_pwd(request):
    upwd = request.POST.get('upwd')

    reseng = UserInfo.objects.filter(upwd=upwd).count() # count  检测是否存在

    context = {'hies': reseng}

    return JsonResponse(context)


def login_yz(request):

    post = request.POST

    uname = post.get('username')
    upwd = post.get('pwd')
    uname_jz = post.get('unamejz', '0')
    print uname_jz

    # 这是加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    context = {'title': '登录', 'uname': uname, 'upwd': upwd, 'top': 0}  # 数据库的存在的结果返回

    user = UserInfo.objects.filter(uname=uname)  # 取出模型的uname

    if len(user) == 0:  # 用户名错误  如果模型没有就是0

        context['name_error'] = '1'  # 给js 传一个参数，

        return render(request, 'booktest/login.html', context)
    else:

        if user[0].upwd == upwd_sha1:  # 查看密码是否正确

            # 记录当前登录用户
            request.session['uid'] = user[0].id
            request.session['uname'] = uname
            print 999

            path = request.session.get('url_path', '/site/')

            response = redirect(path)
            if uname_jz == '1':  # 判断是否记录
                print 66666
                response.set_cookie('uname', uname, expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:
                print "-------"
                response.set_cookie('uname', '', max_age=-1)

            return response

        else:  # 密码错误
            context['pwd_error'] = '1'

            return render(request, 'booktest/login.html', context)


def logout(request):
    request.session.flush()
    return redirect('/login/')


@zhuangshiqi
def site(request):

    user = UserInfo.objects.get(pk=request.session['uid'])  #拿到记录的用户ｕｉｄ

    if request.method == 'POST':
        post = request.POST

        user.ushou = post.get('ushou')
        user.udizhi = post.get('udizhi')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')

        user.save()

    #做一个上下文
    context = {'title': '用户中心', 'user': user}

    #录入的数据要显示在页面
    return render(request, 'booktest/user_center_site.html', context)


@zhuangshiqi
def info(request):

    user = UserInfo.objects.get(pk=request.session['uid'])
    context = {'title': '个人信息', 'user': user}
    return render(request, 'booktest/user_center_info.html', context)


@zhuangshiqi
def order(request):

    context = {'title': '全部订单',  }

    return render(request, 'booktest/user_center_order.html')











































