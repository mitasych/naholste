# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
	(r'^mosaic/choise/$', 'mosaic.views.choise'),
	(ur'^mosaic/option/$', 'mosaic.views.option'),
	(r'^mosaic/uploadfile/$', 'mosaic.views.upload_file'),
	(ur'^mosaic/del/$', 'mosaic.views.delete_file'),
	#(r'^crop/reload/$', 'crop.views.reload'),
	(ur'^mosaic/effect/$', 'mosaic.views.effect'),
)
