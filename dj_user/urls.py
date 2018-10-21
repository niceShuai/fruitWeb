from django.conf.urls import url, include
from dj_user import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^register_handle$', views.register_handle, name='register_handle'),
    url(r'^login$', views.login, name='login'),
    url(r'^user_center_info$', views.user_center_info),
    url(r'^user_center_order$', views.user_center_order),
    url(r'^user_center_site$', views.user_center_site),
]