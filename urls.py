# -*- coding: utf-8 -*-
import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url('', include('account.urls')),
	url('', include('crop.urls')),
	url('', include('mosaic.urls')),
	url('', include('puzzle.urls')),
	url('', include('cart.urls')),
	url('', include('gallery.urls')),
	url('', include('contacts.urls')),
	###
	url(r'^$', 'common.views.index'),
	###
	url(r'^google4d8d225d5b28f671\.html$', 'common.views.google_verif'),
	###
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^favicon\.ico$', RedirectView.as_view(url='/media/favicon.ico')),
	###
	(r'^admin/', include(admin.site.urls)),
	url(r'^chaining/', include('smart_selects.urls')),
)
