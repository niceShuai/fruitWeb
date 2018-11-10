from django.conf.urls import url
from cart import views

urlpatterns = [
    url(r'^cart$', views.cart, name='cart'),
    url(r'^place_order$', views.place_order, name='place_order'),
    url(r'^add_cart$', views.add_cart, name='add_cart'),
    url(r'^edit_goods$', views.edit_goods),
    url(r'del_goods', views.del_goods)
]