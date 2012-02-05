# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
	(r'^cart/show/$', 'cart.views.show'),
	(r'^cart/delivery/$', 'cart.views.delivery'),
	(r'^cart/del/$', 'cart.views.delete'),
	(r'^cart/order/$', 'cart.views.order'),
	(r'^cart/login/$', 'cart.views.log_in'),
)
