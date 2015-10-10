#coding:utf-8
from django.conf.urls import patterns, url
from OrderSystem import views


urlpatterns = patterns('',
    #登陆页面
    url(r'^$', views.login, name='login'),
    #商品清单展示
    url(r'^list/$', views.index, name='list'),
    #商品详情页面
    url(r'^products/(?P<product_pid>[^/]+)/$', 'OrderSystem.views.product_detail', name='product'),
    #历史订单
    url(r'^orderlist/$', views.order, name='orderlist'),
)