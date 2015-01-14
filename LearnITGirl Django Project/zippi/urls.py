from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.zippi_home, name='zippi_home'),
    url(r'^pin/list/$', views.pin_list),
    url(r'^pin/(?P<pk>[0-9]+)/$', views.pin_detail),
    url(r'^pin/new/$', views.pin_new, name='pin_new'),
    url(r'^zippi/register/$', views.register, name='register'),
    url(r'^zippi/login/$', views.user_login, name='login'),
    url(r'^zippi/logout/$', views.user_logout, name='logout'),
)
