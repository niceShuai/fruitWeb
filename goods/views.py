from django.shortcuts import render
from goods.models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    # 选择各类商品传到首页展示，最新商品放四个在大图，点击量最高商品放四个在小字上
    all_type = GoodsType.objects.all()
    fruit_type = all_type.filter(title='新鲜水果')[0]
    fruit  = fruit_type.goodsinfo_set.all()
    fruit_new = fruit.order_by('-id')[:4]
    fruit_click = fruit.order_by('-click')[:4]
    context = {'fruit_new': fruit_new, 'fruit_click': fruit_click, 'fruit_type': fruit_type}
    return render(request, 'goods/index.html', context)

def goods_list(request):
    type = request.GET.get('type')
    sort_flag = request.GET.get('sort_flag')
    page_num = request.GET.get('page_num',1)
    # 获取到商品种类
    goods_type = GoodsType.objects.filter(pk=type)[0]
    goods_alls = goods_type.goodsinfo_set.all()
    # 获取商品排序方式
    # 默认排序：按添加时间
    if sort_flag == '0':
        goods_all = goods_alls.order_by('-id')
    # 价格排序
    elif sort_flag == '1':
        goods_all = goods_alls.order_by('price')
    # 人气排序，按点击量
    elif sort_flag == '2':
        goods_all = goods_alls.order_by('-click')
    else:
        goods_all = goods_alls.order_by('-id')

    # 分页
    paginator = Paginator(goods_all,4)
    page = paginator.page(page_num)

    context = {'goods_all': goods_all, 'page': page, 'type': type}
    return render(request, 'goods/goods_list.html', context)

def detail(request):
    type = request.GET.get('type')
    goods = request.GET.get('goods')
    good = GoodsInfo.objects.filter(type_id=type,id=goods)[0]
    # 每次查询，点击量+1
    good.click += 1
    good.save()
    context = {'good': good}
    return render(request, 'goods/detail.html', context)