from django.conf.urls import url
from goods import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^goods_list$', views.goods_list, name='goods_list'),
    url(r'^detail$', views.detail, name='detail')
]