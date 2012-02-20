# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
	(r'^puzzle/upload/$', 'puzzle.views.upload'),
	(r'^puzzle/uploadfile/$', 'puzzle.views.upload_file'),
	(r'^puzzle/del/$', 'puzzle.views.delete_file'),
	(r'^puzzle/option/$', 'puzzle.views.option'),
	(r'^puzzle/effect/$', 'puzzle.views.effect'),
)
