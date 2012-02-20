# -*- coding: utf-8 -*-
import datetime
import os

from md5 import md5

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import EmailMessage

from collage.account.settings import *
from collage.account.models import User, UserProfile
from collage.account.forms import AuthorizationForm, RegistrationForm, ForgotForm, UserProfileForm

def registration(request):
	user = request.user
	###
	if (user.is_authenticated() and user.is_active):
		return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))
	###
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		###
		if form.is_valid():
			auth_key = md5(str(datetime.datetime.now())).hexdigest()
			###
			send_data = form.cleaned_data
			### Отправка письма
			data = {
				'domain':request.META['HTTP_HOST'],
				'auth_key':auth_key,
			}
			###
			t = loader.get_template('account_registration_mail.html')
			c = RequestContext(request, data)
			html = t.render(c)
			###
			msg = EmailMessage(u'Регистрация на сайте - Фото на холсте', html, EMAIL_FROM, [send_data['email']])
			msg.content_subtype = "html"
			msg.send()
			###
			new_user = User.objects.create_user(
				username = send_data['email'],
				email = send_data['email'],
				password = send_data['password']
			)
			###
			new_user.is_active = False
			new_user.save()
			###
			UserProfile.objects.filter(user=new_user.id).update(
				auth_key=auth_key,
				name=send_data['name'],
				address=send_data['address'],
				phone=send_data['phone']
			)
			###
			messages.success(request, u'На указанный email выслано письмо с кодом подтверждения регистрации')
			###
			return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))
	else:
		initial = {
			'name':request.session.get('name', ''),
			'address':request.session.get('address', ''),
			'phone':request.session.get('phone', ''),
		}
		###
		form = RegistrationForm(initial=initial)
	###
	data = {
		'form':form,
	}
	###
	return render(request, 'account_registration_form.html', data)

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
			messages.success(request, u'Ваша учетная запись активирована<br />Теперь вы можете авторизироваться на сайте')
	###
	return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))

def forgot(request):
	user = request.user
	###
	if (user.is_authenticated() == False):
		if request.method == 'POST':
			form = ForgotForm(request.POST)
			###
			if form.is_valid():
				send_data = form.cleaned_data
				###
				new_password = md5(str(datetime.datetime.now())).hexdigest()[5:13].lower()
				###
				user = User.objects.get(email=send_data['email'])
				user.set_password(new_password)
				user.save()
				###
				data = {
					'new_password':new_password,
				}
				###
				t = loader.get_template('account_forgot_mail.html')
				c = RequestContext(request, data)
				html = t.render(c)
				###
				msg = EmailMessage(u'Фото на холсте - восстановление пароля', html, EMAIL_FROM, [send_data['email']])
				msg.content_subtype = "html"
				msg.send()
				###
				messages.success(request, u'На указанный емаил выслано письмо с новым паролем')
				###
				return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))
		else:
			form = ForgotForm()
	else:
		return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))
	###
	data = {
		'form':form,
	}
	###
	return render(request, 'account_forgot.html', data)

def log_out(request):
	logout(request)
	###
	return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))

def log_in(request):
	user = request.user
	###
	if (user.is_authenticated() == False):
		if request.method == 'POST':
			form = AuthorizationForm(request.POST)
			###
			if form.is_valid():
				send_data = form.cleaned_data
				###
				user = authenticate(username=send_data['email'], password=send_data['password'])
				###
				if user is not None:
					if user.is_active:
						login(request, user)
						###
						return HttpResponseRedirect(reverse('common.views.index'))
					else:
						messages.error(request, u'Ваш профиль заблокирован')
				else:
					messages.error(request, u'Не правильно указан логин или пароль')
			else:
				messages.error(request, u'Ошибка заполнения полей')
		else:
			form = AuthorizationForm()
	else:
		return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))
	###
	data = {
		'form':form,
	}
	###
	return render(request, 'account_log_in.html', data)

def profile(request):
	user = request.user
	###
	if (user.is_authenticated() and user.is_active):
		user_profile = UserProfile.objects.get(user = user.id)
		###
		if request.method == 'POST':
			form = UserProfileForm(request.POST)
			###
			if (form.is_valid()):
				send_data = form.cleaned_data
				###
				UserProfile.objects.filter(user = user.id).update(
					name = send_data['name'],
					address = send_data['address'],
					phone = send_data['phone']
				)
				###
				if not send_data['password'] == '':
					user.set_password(send_data['password'])
					user.save()
				###
				messages.success(request, u'Вашы данные успешно изменены')
		else:
			user_profile = UserProfile.objects.get(user=user.id)
			###
			form = UserProfileForm(instance=user_profile)
		###
		return render(request, 'account_profile.html', locals())
	else:
		return HttpResponseRedirect(reverse(DEFAULT_REDIRECT))
