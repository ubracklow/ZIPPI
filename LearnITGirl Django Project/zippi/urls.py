from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.zippi_start, name='zippi_start'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^login/deleteprofile/$', views.delete_profile, name='delete_profile'),
    url(r'^home/$', views.zippi_home, name='zippi_home'),
    url(r'^newmap/$', views.new_map, name='new_map'),
    url(r'^maplist/$', views.map_list, name='map_list'),
    url(r'^mymap/(?P<pk>[0-9]+)/$', views.my_map, name='my_map'),
    url(r'^mymap/(?P<pk>[0-9]+)/delete/$', views.delete_map, name='delete_map'),
    url(r'^pin/new/(?P<pk>[0-9]+)/$', views.new_pin, name='new_pin'),
    url(r'^pinlist/(?P<pk>[0-9]+)/$', views.pin_list, name='pin_list'),
    url(r'^pin/(?P<pk>[0-9]+)/$', views.pin_detail, name='pin_detail'),
    url(r'^pin/(?P<pk>[0-9]+)/edit/$', views.pin_edit, name='pin_edit'),
    url(r'^pin/(?P<pk>[0-9]+)/delete/$', views.pin_delete, name='pin_delete'),
    
)
