# -*- coding: utf-8 -*-
import datetime
from django.template import RequestContext
from django import template
from collage.account.models import UsersOnline

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

def user_online(context):
	request = context['request']
	user = context['request'].user
	###
	datetime_now = datetime.datetime.now()
	###
	client_address = request.META['REMOTE_ADDR']
	###
	if user.is_authenticated():
		usr = UsersOnline.objects.filter(username=user)
		###
		if usr.exists():
			usr.update(time=datetime_now)
		else:
			UsersOnline(username=user, time=datetime_now).save()
	else:
		usr = UsersOnline.objects.filter(username=user, ip_adress=client_address)
		###
		if usr.exists():
			usr.update(time=datetime_now)
		else:
			UsersOnline(username=user, ip_adress=client_address, time=datetime_now).save()
	###
	online_users = UsersOnline.objects.all()
	###
	for users in online_users:
		if ((datetime_now - users.time) > datetime.timedelta(minutes=3)):
			users.delete()
	###
	return {'online_users': online_users}

register.inclusion_tag('templatetags/header.html', takes_context=True)(header)
register.inclusion_tag('templatetags/footer.html')(footer)
register.inclusion_tag('templatetags/menu.html')(menu)
register.inclusion_tag('templatetags/user_online.html', takes_context=True)(user_online)
