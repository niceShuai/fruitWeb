from hashlib import md5

from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
# Create your views here.

from users.models import *
from goods.models import *

from users.login_verify import *

def register(request):
    return render(request, 'users/register.html')

# 用ajax判断注册时用户名是否存在于数据库中
def register_search(request):
    # uname为注册时用户输入的用户名
    uname = request.GET.get('uname', None)
    print(uname)
    # 查询数据库是否存在该数据
    flag = UserInfo.objects.filter(user_name=uname).exists()
    print(flag)
    return JsonResponse({"flag":flag})

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
        return redirect('users:login')
    else:
        return redirect('users:register')

def login(request):
    # 获取存在cookie里的用户名
    u_name = request.COOKIES.get('u_name','')
    context = {'error_flag':0, 'u_name': u_name}
    return render(request, 'users/login.html', context)

def login_handel(request):
    # 接收登陆页面用户输入的用户名和密码
    u_name = request.POST.get('username','')
    u_pwd = request.POST.get('pwd','')
    user_info = UserInfo.objects.filter(user_name=u_name)
    # 如果在数据库中找到了该用户名
    if len(user_info) != 0:
        # 将登陆时输入的密码加密与数据库中密码做比较
        u_pwd_str = str(u_pwd)
        m = md5()
        m.update(u_pwd_str.encode('utf-8'))
        u_pwd_md5 = m.hexdigest()
        if u_pwd_md5 == user_info[0].user_pwd:
            # 验证成功后，将用户名存储至session，建立会话保持
            remember_name = request.POST.get('remember_name', '')
            request.session['u_name'] = u_name
            request.session.set_expiry(6000)
            # 执行登陆验证的装饰器后，将请求地址存到了url的cookie里，这里取出来重定向回去
            # 这样用户回到登陆前请求的页面
            url = request.COOKIES.get('url', '/')
            hrr = HttpResponseRedirect(url)
            # 如果remember_name==1，则将用户名存储至cookie
            if remember_name != '':
                hrr.set_cookie('u_name', u_name)
            else:
                hrr.set_cookie('u_name','', max_age=-1)
            # 转到用户信息界面
            return hrr
        else:
            # 如果用户名错误，则仍在登陆页面，把输入的错误用户名显示在text框内
            context = {'u_name': u_name, 'error_flag':1}
            return render(request, 'users/login.html', context)
    # 如果在数据库中没有找到该用户名
    else:
        context = {'u_name': u_name, 'error_flag': 1}
        return render(request, 'users/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

@verify
def user_center_info(request):
    recent_review_ids = request.COOKIES.get('recent_review_ids', [])

    goods_all = []

    # 将要传递给最近浏览页面的数据存储到列表goods_all里
    if recent_review_ids != []:
        recent_review_ids = eval(recent_review_ids)

        for temp in recent_review_ids:
            goods = GoodsInfo.objects.get(id=temp)
            goods_all.append(goods)

    # 传递上下文，如果cookie里没有值，则上下文为空列表 []
    context = {'goods_all': goods_all}
    return render(request, 'users/user_center_info.html', context)

@verify
def user_center_order(request):
    return render(request, 'users/user_center_order.html')

@verify
def user_center_site(request):
    return render(request, 'users/user_center_site.html')