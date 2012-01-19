# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
	(r'^crop/upload/$', 'crop.views.upload'),
	(ur'^crop/option/(?P<file_id>[a-z,0-9]{32})/$', 'crop.views.option'),
	(r'^crop/uploadfile/$', 'crop.views.upload_file'),
	(ur'^crop/del/(?P<file_id>[a-z,0-9]{32})/$', 'crop.views.delete_file'),
	(r'^crop/reload/$', 'crop.views.reload'),
	(ur'^crop/effect/(?P<file_id>[a-z,0-9]{32})/$', 'crop.views.effect'),
)
