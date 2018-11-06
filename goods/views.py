from django.shortcuts import render
from goods.models import *
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.template import loader, RequestContext
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
    type = request.GET.get('type', 1)
    sort_flag = request.GET.get('sort_flag', 0)
    page_num = request.GET.get('page_num', 1)
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
    type = request.GET.get('type', 1)
    goods = request.GET.get('goods', 1)
    good = GoodsInfo.objects.filter(id=goods)[0]
    # 每次查询，点击量+1
    good.click += 1
    good.save()

    t1 = loader.get_template('goods/detail.html')
    context = {'good': good}
    http_res = HttpResponse(t1.render(context))

    # 增加最近浏览功能，用户每次点击的商品id存入cookie，最多存储五个id。
    # 本次点击的商品的id
    recent_review_id = int(goods)

    # 存储商品id的cookie，是一个list
    recent_review_ids = request.COOKIES.get('recent_review_ids', [])

    if recent_review_ids != []:
        # 如果存储商品id的cookie不是空，把当前商品id insert到列表第一位，然后写入cookie
        recent_review_ids = eval(recent_review_ids) # cookie取出来是"[ , ]",用此函数转化为[ , ]
        if recent_review_id in recent_review_ids:
            # 如果本次点击商品的id已存在于cookie中，则删除，然后insert到第0位
            recent_review_ids.remove(recent_review_id)
        recent_review_ids.insert(0,recent_review_id)

        # 最近浏览只存五个
        if len(recent_review_ids) > 5:
            del recent_review_ids[5]

    else:
        # 如果存储商品id的cookie是空，则将本次点击的商品的id存入列表后，存入cookie
        recent_review_ids.insert(0, recent_review_id)

    # print(recent_review_ids)
    http_res.set_cookie('recent_review_ids', recent_review_ids)


    return http_res