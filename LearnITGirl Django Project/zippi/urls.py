from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.zippi_start, name='zippi_start'),
    url(r'^pin/list/$', views.pin_list),
    url(r'^pin/(?P<pk>[0-9]+)/$', views.pin_detail),
    url(r'^pin/new/$', views.pin_new, name='pin_new'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^showmap/(?P<pk>[0-9]+)/$', views.show_map, name='show_map'),
    url(r'^pinsearch/$', views.pin_search, name='pin_search'),
    url(r'^mapcenter/$', views.map_center, name='map_center'),
    
)
