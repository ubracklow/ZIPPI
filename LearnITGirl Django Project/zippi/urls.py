from django.conf.urls import patterns, include, url
from . import views

#maps https://bitbucket.org/dbinit/django-gmapi/
#from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', views.zippi_start, name='zippi_start'),
    url(r'^pin/list/$', views.pin_list),
    url(r'^pin/(?P<pk>[0-9]+)/$', views.pin_detail),
    url(r'^pin/new/$', views.pin_new, name='pin_new'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^maptest/$', views.map_test, name='zippi_maptest'),
    
    #maps https://bitbucket.org/dbinit/django-gmapi/
    #(r'', include('gmapi.urls.media')), # Use for debugging only.
    #(r'mymap/^$', 'mymapp.views.index'),
)
