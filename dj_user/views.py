from hashlib import md5

from django.shortcuts import render, redirect
# Create your views here.

from dj_user.models import *

def register(request):
    return render(request, 'dj_user/register.html')

def register_handle(request):
    pwd1 = request.POST.get('pwd')
    pwd2 = request.POST.get('cpwd')
    print(pwd1)
    print(request.POST.get('user_name'))
    # 判断两次密码是否相同
    if pwd1 == pwd2:
        # 若相同，进行mad5加密
        pwd_str = str(pwd1)
        m = md5()
        m.update(pwd_str.encode('utf-8'))
        pwd3 = m.hexdigest()
        # 创建user对象，存入表单传来的user信息。
        user = UserInfo()
        user.user_name = request.POST.get('user_name')
        user.user_email = request.POST.get('email')
        user.user_pwd = pwd3
        user.save()
        return redirect('dj_user:login')
    else:
        return redirect('dj_user:register')

def login(request):
    return render(request, 'dj_user/login.html')

