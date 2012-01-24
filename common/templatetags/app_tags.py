# -*- coding: utf-8 -*-

from django import template

register = template.Library()

def my_app_name(app_name):
	try:
		app = __import__(app_name.lower())
		###
		return app.app_label
	except:
		return app_name

my_app_name = register.simple_tag(my_app_name)
