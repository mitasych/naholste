# -*- coding: utf-8 -*-
from settings import *
from django import forms
from django.forms.util import ErrorList
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from collage.account.models import UserProfile

class FormErrorList(ErrorList):
	def __unicode__(self):
		return self.as_divs()

	def as_divs(self):
		if not self:
			return u''
		###
		return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])

class AuthorizationForm(forms.Form):
	user = forms.CharField(label="Пользователь", error_messages={'required': u'Введите имя'})
	password = forms.CharField(widget=forms.PasswordInput, label="Пароль", error_messages={'required': u'Введите пароль'})

class RegistrationForm(forms.Form):
	user = forms.CharField(label="Пользователь", error_messages={'required': u'Укажите логин'})
	password = forms.CharField(widget=forms.PasswordInput, label="Пароль", error_messages={'required': u'Укажите пароль'})
	email = forms.EmailField(required=True, error_messages={'invalid': u'Укажите корректный e-mail', 'required': u'Укажите e-mail'})
	captcha = CaptchaField(label="Капча", error_messages={'required': u'Введите цифры с картинки','invalid': u'Неверно указан код'})

	def clean_user(self):
		user = self.cleaned_data['user']
		###
		if len(user) > 30:
			raise forms.ValidationError("Не больше 30 символов")
		###
		if User.objects.filter(username=user).exists():
			raise forms.ValidationError("Такой пользователь уже есть")
		else:
			return user

	def clean_email(self):
		email = self.cleaned_data['email']
		###
		if len(email) > 40:
			raise forms.ValidationError("Не больше 40 символов")
		###
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Такой емаил уже есть")
		else:
			return email

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		###
		self.error_class = self.RefistrationFormErrorList

	class RefistrationFormErrorList(ErrorList):
		def __unicode__(self):
			return self.as_divs()

		def as_divs(self):
			if not self:
				return u''
			###
			return u'<div class="errorlist_registration">%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('avatar', 'gender', 'about',)
		widgets = {'about': forms.Textarea(attrs={'class': 'textarea',}),}
