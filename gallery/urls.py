# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
	(r'^gallery/albums/$', 'gallery.views.albums'),
	(r'^gallery/images/$', 'gallery.views.images'),
	(r'^gallery/crop/$', 'gallery.views.to_crop'),
)
