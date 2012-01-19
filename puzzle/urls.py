# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
	(r'^puzzle/upload/$', 'puzzle.views.upload'),
	(ur'^puzzle/option/(?P<file_id>[a-z,0-9]{32})/$', 'puzzle.views.option'),
	(r'^puzzle/uploadfile/$', 'puzzle.views.upload_file'),
	(ur'^puzzle/del/(?P<file_id>[a-z,0-9]{32})/$', 'puzzle.views.delete_file'),
	(r'^puzzle/reload/$', 'puzzle.views.reload'),
	(ur'^puzzle/effect/(?P<file_id>[a-z,0-9]{32})/$', 'puzzle.views.effect'),
)
