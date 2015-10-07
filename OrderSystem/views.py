#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from .models import User
from django import forms

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
                    return render_to_response('success.html')
                else:
                    return render_to_response('login.html', {'userform':userform, 'error':'密码错误！'})
    else:
        userform = UserForm()
    return render_to_response('login.html', {'userform':userform})

# Create your views here.
