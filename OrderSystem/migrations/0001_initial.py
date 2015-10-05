# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='商品数量')),
            ],
            options={
                'verbose_name_plural': '订单详情',
                'verbose_name': '订单详情',
            },
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('listid', models.IntegerField(serialize=False, auto_created=True, primary_key=True, verbose_name='订单ID', editable=False)),
                ('date', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('shipcost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='运费')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总价格')),
            ],
            options={
                'verbose_name_plural': '历史订单',
                'verbose_name': '历史订单',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(serialize=False, auto_created=True, primary_key=True, verbose_name='商品ID', editable=False)),
                ('name', models.CharField(max_length=256, verbose_name='品名')),
                ('picture', models.ImageField(upload_to='', verbose_name='图片')),
                ('weight', models.IntegerField(verbose_name='重量')),
                ('retail', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='零售价')),
                ('intro', models.TextField(default='', verbose_name='介绍')),
            ],
            options={
                'verbose_name_plural': '商品',
                'verbose_name': '商品',
            },
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('type', models.IntegerField(serialize=False, auto_created=True, primary_key=True, verbose_name='运输方式', editable=False)),
                ('shipname', models.CharField(max_length=50, verbose_name='运输名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
            ],
            options={
                'verbose_name_plural': '运输方式',
                'verbose_name': '运输方式',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.IntegerField(serialize=False, auto_created=True, primary_key=True, verbose_name='用户ID', editable=False)),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
            },
        ),
        migrations.AddField(
            model_name='orderlist',
            name='ship',
            field=models.OneToOneField(verbose_name='运输方式', to='OrderSystem.Ship'),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='user',
            field=models.ForeignKey(to='OrderSystem.User', verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='orderid',
            field=models.ForeignKey(to='OrderSystem.OrderList', verbose_name='订单ID'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='productid',
            field=models.ForeignKey(to='OrderSystem.Product', verbose_name='商品ID'),
        ),
    ]
