from django.shortcuts import render
from django.http.response import JsonResponse

from cart.models import *
from users.login_verify import *
from users.models import *
from goods.models import *

# Create your views here.
@verify
def cart(request):
    u_id = int(request.session.get('u_id'))
    carts = Cart.objects.filter(user=u_id)
    context = {'carts': carts}
    return render(request, 'cart/cart.html', context)

def place_order(request):
    return render(request, 'cart/place_order.html')

@verify # add_cart是ajax的请求，用装饰器来判断登陆是全页面更新，无法起作用。所以要在js中判断登陆。
def add_cart(request):
    # 在商品详情页点击加入购物车后，创建购物车对象，存入用户id，商品id，商品数量
    u_id = int(request.session.get('u_id'))
    add_id = int(request.GET.get('add_id'))
    add_num = int(request.GET.get('add_num'))
    # 查询用户要加入购物车的商品是否已存在
    carts = Cart.objects.filter(user=u_id, goods=add_id)
    if len(carts) != 0:
        # 如果商品在购物车已存在，则购物车里数量加上呀添加的数量
        cart = carts[0]
        cart.count += add_num
    else:
        # 如果商品在购物车中不存在，则创建cart对象，添加一条购物车信息
        cart = Cart()
        cart.user = UserInfo.objects.filter(id=u_id)[0]
        cart.goods = GoodsInfo.objects.filter(id=add_id)[0]
        cart.count = add_num
    cart.save()

    # if request.is_ajax():
    count = Cart.objects.filter(user=u_id).count()
    return JsonResponse({'count': count})

def edit_goods(request):
    id = request.GET.get('id')
    num = request.GET.get('num')
    cart = Cart.objects.filter(id=id)[0]
    cart.count = num
    cart.save()
    return JsonResponse(None)

def del_goods(request):
    try:
        id = request.GET.get('id')
        Cart.objects.filter(id=id).delete()
        context = {"flag": 1}
    except:
        context = {"flag": 0}
    return JsonResponse(context)