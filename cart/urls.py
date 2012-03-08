# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
	(r'^cart/show/$', 'cart.views.show'),
	(r'^cart/del/$', 'cart.views.delete'),
	(r'^cart/shiping/$', 'cart.views.shiping'),
	(r'^cart/login/$', 'cart.views.log_in'),
	(r'^cart/order/$', 'cart.views.order'),
	(r'^cart/payment/$', 'cart.views.payment'),
	(r'^payment/kzcom/notify/$', 'cart.views.kzcom'),
	(r'^payment/webmoney/notify/$', 'cart.views.webmoney'),
)
