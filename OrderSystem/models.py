#coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse

class Product(models.Model):
    pid = models.IntegerField('商品ID', primary_key=True, auto_created=True, editable=False)
    name = models.CharField('品名', max_length=256)
    picture = models.ImageField('图片', upload_to='./common_static/pic')
    weight = models.IntegerField ('重量')
    retail = models.DecimalField('零售价', decimal_places=2, max_digits=10)
    intro = models.TextField('介绍', default='')

    def get_absolute_url(self):
        return reverse('product', args=(str(self.pid),))

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = '商品'
        verbose_name_plural = '商品'

class User(models.Model):
    uid = models.IntegerField('用户ID', primary_key=True, auto_created=True, editable=False)
    username = models.CharField('用户名', max_length=50)
    password = models.CharField('密码', max_length=50)

    def __str__(self):
        return self.username

    class Meta():
        verbose_name = '用户'
        verbose_name_plural = '用户'

class Ship(models.Model):
    type = models.IntegerField('运输方式', primary_key=True, auto_created=True,editable=False)
    shipname = models.CharField('运输名称', max_length=50)
    price = models.DecimalField('单价', decimal_places=2, max_digits=10)

    def __str__(self):
        return self.shipname

    class Meta():
        verbose_name = '运输方式'
        verbose_name_plural = '运输方式'

class OrderList(models.Model):
    listid = models.IntegerField('订单ID', primary_key=True, auto_created=True, editable=False)
    user = models.ForeignKey(User, verbose_name='用户名')
    date = models.DateTimeField('创建时间', auto_now_add=True)
    ship = models.ForeignKey(Ship, verbose_name='运输方式')
    shipcost = models.DecimalField('运费', decimal_places=2, max_digits=10)
    total = models.DecimalField('总价格', decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.listid)

    class Meta():
        verbose_name = '历史订单'
        verbose_name_plural = '历史订单'

class OrderDetail(models.Model):
    orderid = models.ForeignKey(OrderList, verbose_name='订单ID')
    productid = models.ForeignKey(Product, verbose_name='商品ID')
    amount = models.IntegerField('商品数量')

    class Meta():
        verbose_name = '订单详情'
        verbose_name_plural = '订单详情'

# Create your models here.
