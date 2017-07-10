# coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator

# Create your views here.


def index(request):

    goods_list = []

    typeinfo = TypeInfo.objects.all()#拿到商品类的所有分类
    for t1 in typeinfo:  # 遍历所欲分类　t1
        nlist = t1.goodsinfo_set.order_by('-id')[0:4]  #拿最新的４个
        clist = t1.goodsinfo_set.order_by('-gclick')[0:4]
        goods_list.append({'t1': t1, 'nlist': nlist, 'clist': clist})

    context = {'title': '首页', 'glist': goods_list, 'top':'2'}

    return render(request, 'ttsx_goods/index.html', context)


def list(request, tid, pid):
    t1 = TypeInfo.objects.get(pk=int(tid))
    new_list = t1.goodsinfo_set.order_by('-id')[0:2] # 新品拿到后两个

    #查询当前分类的所有数据，每页15个

    lang = t1.goodsinfo_set.order_by('-id')  # 获取所有数据
    paginator = Paginator(lang, 1)  #每页数据多少个
    pidx = int(pid)

    if pidx < 1:
        pidx = 1
    elif pidx > paginator.num_pages:
        pidx = paginator.num_pages
    page = paginator.page(pidx)

    context = {'title': '商品详情', 't1': t1, 'top': '2', 'new_list': new_list, 'page1': page}

    return render(request, 'ttsx_goods/list.html', context)


def detail(request):
    return render(request, 'ttsx_goods/detail.html')
