# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
	response = render(request, 'common_index.html', [])
	###
	return response
	
def google_verif(request):
	response = render(request, 'google4d8d225d5b28f671.html', [])
	###
	return response
