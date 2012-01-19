# -*- coding: utf-8 -*-
import datetime
import os

from settings import *
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q 
from django.utils.html import escape
from django.core.urlresolvers import reverse
from django.db.models import signals
from md5 import md5

from collage.account.models import *
from collage.account.forms import *
from collage.common.helpers import Img

TEMPLATE = ''
EMAIL_FROM = 'aries.forum@gmail.com'
REGISTRATION_VIA_EMAIL = 'yes'
###
DEFAULT_REDIRECT = 'common.views.index'

def registration(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		###
		if form.is_valid():
			from django.core.mail import send_mail
			###
			auth_key = md5(str(datetime.datetime.now())).hexdigest()
			send_data = form.cleaned_data
			host = request.META['HTTP_HOST']
			subject = u'Aries example registration'
			email_from = EMAIL_FROM
			email = send_data['email']
			message = ''.join([u'Добро пожаловать ', send_data['user'], u'\n\n', u'Код авторизации ', 'http://', host, 'registration/confirm/', auth_key])
			###
			send_mail(subject, message, email_from, [email])
			###
			new_user = User.objects.create_user(
				username = send_data['user'],
				email = send_data['email'],
				password = send_data['password']
			)
			###
			new_user.is_active = False
			new_user.save()
			###
			UserProfile.objects.filter(user=new_user.id).update(auth_key=auth_key)
			###
			request.session['success'] = ''.join([u'Спасибо ', send_data['user'], u'. На ваш емаил: ', email, u' отправлено письмо с кодом. <br /><br /><a href="/">На главную</a>'])
			###
			return HttpResponseRedirect(reverse('account.views.registration_success'))
	else:
		form = RegistrationForm()
	###
	return render(request, 'account_registration_form.html', locals())

def registration_success(request):
	if request.session.get('success', False):
		success = request.session['success']
		###
		del request.session['success']
	else:
		return HttpResponseRedirect(reverse('account.views.registration'))
	###
	return render(request, 'account_success.html', locals())

def registration_confirm(request, auth_key):
	if UserProfile.objects.filter(auth_key=auth_key).exists():
		user = UserProfile.objects.get(auth_key=auth_key).user
		###
		if user.is_active == True:
			return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))
		else:
			user_profile = UserProfile.objects.get(user=user.id)
			###
			user.is_active = True
			user.save()
			###
			user_profile.auth_key = '-==KEY-CONFIRMED==-'
			user_profile.save()
			###
			success = u'Ваша учетная запись активирована.<br /><br /><a href="/">На главную</a>'
			###
			return render(request, 'account_success.html', {'success': success})
	else:
		return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))

def log_out(request):
	logout(request)
	###
	return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))

def log_in(request):
	user = request.user
	###
	if (user.is_authenticated() == False):
		if request.method == 'POST':
			form = AuthorizationForm(request.POST, error_class=FormErrorList)
			###
			if form.is_valid():
				send_data = form.cleaned_data
				###
				user = authenticate(username=send_data['user'], password=send_data['password'])
				###
				if user is not None:
					if user.is_active:
						login(request, user)
						###
						return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))
					else:
						auth_error = 'Ваш профиль заблокирован'
				else:
					auth_error = 'Не првильно указан логин или пароль'
		else:
			form = AuthorizationForm()
	else:
		return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))
	###
	return render(request, 'account_log_in.html', locals())

def view(request, profile):
	if User.objects.filter(username=profile).exists():
		user = User.objects.get(username=profile)
		user_profile = UserProfile.objects.get(user=user.id)
		###
		return render(request, 'account_view.html', locals())
	else:
		return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))

def profile(request):
	user = request.user
	###
	if (user.is_authenticated() and user.is_active):
		datetime_now = datetime.datetime.now()
		###
		user_profile = UserProfile.objects.get(user = user.id)
		###
		if request.method == 'POST':
			form = UserProfileForm(request.POST, request.FILES, error_class=FormErrorList)
			###
			if (form.is_valid()):
				send_data = form.cleaned_data
				###
				img = Img().resize(request.FILES, 'avatar')
				###
				if img:
					if user_profile.avatar:
						old = '%s/avatar/%s' % (MEDIA_ROOT, user_profile.avatar,)
						###
						if os.path.isfile(old):
							os.remove(old)
					###
					file_name = md5(''.join([str(user.id), str(datetime.datetime.now()),])).hexdigest()
					file_name = ''.join([file_name, '.jpg'])
					###
					img.save('%s/avatar/%s' % (MEDIA_ROOT, file_name,), "JPEG")
					###
					UserProfile.objects.filter(user = user.id).update(
						avatar = file_name,
						gender = send_data['gender'],
						about = send_data['about']
					)
				else:
					UserProfile.objects.filter(user = user.id).update(
						gender = send_data['gender'],
						about = send_data['about']
					)
				###
				return HttpResponseRedirect(reverse('account.views.view', args=(user.username,)))
		else:
			form = UserProfileForm(initial = {'gender': user_profile.gender, 'about': user_profile.about,})
		###
		return render(request, 'account_profile.html', locals())
	else:
		return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))
