from django.shortcuts import redirect
from django.http.response import HttpResponseRedirect

def verify(func):
    def inner(request):
        if 'u_name' in request.session:
            return func(request)
        else:
            res = HttpResponseRedirect('/user/login')
            # 将请求地址存储只cookie，完成登陆后重定向回请求时的地址
            res.set_cookie('url', request.get_full_path())
            return res
    return inner
