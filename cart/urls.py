# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
	(r'^cart/show/$', 'cart.views.show'),
	(r'^cart/del/$', 'cart.views.delete'),
)
