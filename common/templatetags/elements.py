# -*- coding: utf-8 -*-
from django import template

register = template.Library()

def header(context):
	user = context['request'].user
	###
	if user.is_authenticated():
		return {'auth': True, 'username': user.username}
	else:
		return {'auth': False, 'username': 'Гость'}

def footer():
	return {}
	
def menu():
	return {}

register.inclusion_tag('templatetags/header.html', takes_context=True)(header)
register.inclusion_tag('templatetags/footer.html')(footer)
register.inclusion_tag('templatetags/menu.html')(menu)
