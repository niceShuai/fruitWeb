from django.shortcuts import render
from django.http.response import JsonResponse

from cart.models import *
from users.login_verify import *
from users.models import *
from goods.models import *

# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')

def place_order(request):
    return render(request, 'cart/place_order.html')

@verify
def add_cart(request):
    # 在商品详情页点击购买后，创建购物车对象，存入用户id，商品id，商品数量
    u_id = int(request.session.get('u_id'))
    add_id = int(request.GET.get('add_id'))
    add_num = int(request.GET.get('add_num'))
    cart = Cart()
    cart.user = UserInfo.objects.filter(id=u_id)[0]
    cart.goods = GoodsInfo.objects.filter(id=add_id)[0]
    cart.count = add_num
    cart.save()

    if request.is_ajax():
        count = Cart.objects.filter(user=u_id).count()
        print(count)

    return JsonResponse({'count': count})