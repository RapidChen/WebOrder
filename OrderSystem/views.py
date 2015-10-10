#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django import forms

#尝试在cookie中获取用户名，不成功则跳转到登陆页面
def checkcookie(request):
    try:
        username =  request.COOKIES['username']
    except:
        return None
    else:
        return username

#定义用户表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

#登陆功能
def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            #获取用户名密码
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            #将获取的表单与数据库作比较
            try:
                user = User.objects.get(username = username)
            except:
                return render_to_response('login.html', {'userform':userform, 'error':'用户名不存在！'})
            else:
                if user.password == password:
                    response = render_to_response('success.html')
                    response.set_cookie('username', username, 3600)
                    return response
                else:
                    return render_to_response('login.html', {'userform':userform, 'error':'密码错误！'})
    else:
        userform = UserForm()
    return render_to_response('login.html', {'userform':userform})

#主页
def index(request):
    username = checkcookie(request)
    if username == None:
        return HttpResponseRedirect('/')
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

#商品
def product_detail(request, product_pid):
    username = checkcookie(request)
    if username == None:
        return HttpResponseRedirect('/')
    product = Product.objects.get(pid = product_pid)
    product.picture = str(product.picture).replace('common_','/')
    return render(request, 'product.html', {'product': product})

#历史订单
def order(request):
    username = checkcookie(request)
    if username == None:
        return HttpResponseRedirect('/')
    orders = OrderList.objects.filter(user__username = username)
    return render(request, 'orderlist.html', {'orders': orders})

# Create your views here.
