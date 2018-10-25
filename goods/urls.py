from django.conf.urls import url
from goods import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^list$', views.list, name='list'),
    url(r'^detail$', views.detail, name='detail')
]