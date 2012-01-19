# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
	(r'^registration/$', 'account.views.registration'),
	(r'^registration/success/$', 'account.views.registration_success'),
	(r'^registration/confirm/(?P<auth_key>[a-z,0-9]+)/$', 'account.views.registration_confirm'),
	(r'^account/logout/$', 'account.views.log_out'),
	(r'^account/login/$', 'account.views.log_in'),
	(ur'^account/view/(?P<profile>\D.+)/$', 'account.views.view'),
	(u'^account/profile/$', 'account.views.profile'),
)
