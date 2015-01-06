from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.pin_list),
    url(r'^pin/(?P<pk>[0-9]+)/$', views.pin_detail),
    url(r'^pin/new/$', views.pin_new, name='pin_new'),
)
