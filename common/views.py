# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
	response = render(request, 'common_index.html', [])
	###
	return response
