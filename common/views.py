# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse

from collage.common.helpers import CookieListFiles

def index(request):
	#clf = CookieListFiles()
	#data = clf.get(request)
	###
	response = render(request, 'common_index.html', [])
	###
	"""if len(data) == 0:
		f = []
		###
		f.append('file1')
		f.append('file2')
		f.append('file3')
		###
		clf.set(response, f)"""
	###
	return response
