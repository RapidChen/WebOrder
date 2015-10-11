#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,Http404
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

def iniCart(response):
    products = Product.objects.all()
    for product in products:
        response.set_cookie(str(product.pid), 0)
    return response

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
                    response = iniCart(response)
                    return response
                else:
                    return render_to_response('login.html', {'userform':userform, 'error':'密码错误！'})
    else:
        username = checkcookie(request)
        if username != None:
            return HttpResponseRedirect('/list/')
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
    info = ''
    username = checkcookie(request)
    if username == None:
        return HttpResponseRedirect('/')
    product = Product.objects.get(pid = product_pid)
    product.picture = str(product.picture).replace('common_','/')
    response = render(request, 'product.html', {'product': product, 'info':info})
    if request.method == 'POST':
        amount = request.POST['amount']
        if amount ==  '':
            return response
        response = render(request, 'success1.html')
        amount0 = int(request.COOKIES[str(product_pid)])
        amount = int(amount) + amount0
        response.set_cookie(str(product_pid), amount)
        return response
    return response

#历史订单
def order(request):
    username = checkcookie(request)
    if username == None:
        return HttpResponseRedirect('/')
    orders = OrderList.objects.filter(user__username = username)
    return render(request, 'orderlist.html', {'orders': orders})

#订单详情
def order_detail(request, order_listid):
    username = checkcookie(request)
    if username == None:
        return HttpResponseRedirect('/')
    try:
        order = OrderList.objects.get(listid = order_listid)
    except:
        raise Http404
    if username != order.user.username:
        raise Http404
    details = OrderDetail.objects.filter(orderid = order_listid)
    return render(request, 'order.html', {'order': order, 'details': details})

#登出
def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    return response

#购物车
def cart(request):
    cart0 = []
    username = checkcookie(request)
    if username == None:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        selects = []
        products = Product.objects.all()
        for product in products:
            try:
                selects.append(request.POST[str(product.pid)])
            except:
                pass
        if not selects:
            return render_to_response('fail.html', {'error':'未选择商品或者购物车为空！'})
        response = render(request, 'success1.html')
        for select in selects:
            response.set_cookie(select, 0)
        return response
    products = Product.objects.all()
    total = 0
    weight = 0
    for product in products:
        amount =  int(request.COOKIES[str(product.pid)])
        if amount != 0:
            product.amount = amount
            total += (product.retail * amount)
            weight += (product.weight * amount)
            cart0.append(product)
        air = weight * Ship.objects.get(shipname='空运').price
        land = weight * Ship.objects.get(shipname='陆运').price
    return render(request, 'cart.html', {'products': cart0, 'total': total, 'weight':weight, 'air':air, 'land':land})

def empty(request):
    username = checkcookie(request)
    if username == None:
        return HttpResponseRedirect('/')

    products = Product.objects.all()
    for product in products:
        if int(request.COOKIES[str(product.pid)]):
            response = render(request, 'success1.html')
            response = iniCart(response)
            return response
    return render_to_response('fail.html', {'error':'购物车已经为空！'})
# Create your views here.
