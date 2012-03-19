# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
	(r'^crop/upload/$', 'crop.views.upload'),
	(r'^crop/uploadfile/$', 'crop.views.upload_file'),
	(r'^crop/upload_progress/$', 'crop.views.upload_progress'),
	(r'^crop/del/$', 'crop.views.delete_file'),
	(r'^crop/option/$', 'crop.views.option'),
	(r'^crop/effect/$', 'crop.views.effect'),
)
