# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include


urlpatterns = patterns('',
    (r'^socauth/$', 'socauth.views.home'),
    (r'^socauth/done/$', 'socauth.views.done'),
    (r'^socauth/error/$', 'socauth.views.error'),
    (r'^socauth/logout/$', 'socauth.views.logout'),
    (r'^socauth/form/$', 'socauth.views.form'),
)
