# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
	(r'^account/registration/$', 'account.views.registration'),
	(r'^account/registration/confirm/(?P<auth_key>[a-z,0-9]+)/$', 'account.views.registration_confirm'),
	(r'^account/logout/$', 'account.views.log_out'),
	(r'^account/login/$', 'account.views.log_in'),
	(r'^account/forgot/$', 'account.views.forgot'),
	(u'^account/profile/$', 'account.views.profile'),
)
