# coding=utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class TypeInfo(models.Model):

    ttitle = models.CharField(max_length=20) # 全部商品标题

    isDelete=models.BooleanField(default=False)

    def __str__(self):

        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):

    gtitle = models.CharField(max_length=50) #商品名字

    gpic = models.ImageField(upload_to='goods') # 商品图片对应goods目录

    gprice = models.DecimalField(max_digits=5, decimal_places=2)  # 浮点数　　价格

    gclick = models.IntegerField(default=0) # 整数　点击量

    gunit = models.CharField(max_length=20)   #单位500g

    isDelete = models.BooleanField(default=False) # 布尔字段　返回t和f

    gsubtitle = models.CharField(max_length=200) # 副标题

    gkucun = models.IntegerField(default=100) #库存

    gcontent = HTMLField() # 商品详情

    gtype =models.ForeignKey('TypeInfo') # 一对多的关系





