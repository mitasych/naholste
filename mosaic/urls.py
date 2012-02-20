# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
	(r'^mosaic/choise/$', 'mosaic.views.choise'),
	(r'^mosaic/create/$', 'mosaic.views.create'),
	(r'^mosaic/del/$', 'mosaic.views.delete_file'),
	(r'^mosaic/option/$', 'mosaic.views.option'),
	(r'^mosaic/uploadfile/$', 'mosaic.views.upload_file'),
	(ur'^mosaic/effect/$', 'mosaic.views.effect'),
)
