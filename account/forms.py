# -*- coding: utf-8 -*-
import re

from django import forms
from django.forms.util import ErrorList
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from collage.account.settings import *
from collage.account.models import UserProfile

class FormErrorList(ErrorList):
	
	def __unicode__(self):
		return self.as_tr()

	def as_tr(self):
		if not self:
			return u''
		###
		return u'%s' % ''.join([u'<tr><td colspan="2" width="335" class="tr_error">%s</td></tr>' % e for e in self])

class BaseAccountForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(BaseAccountForm, self).__init__(*args, **kwargs)
		###
		self.error_class = FormErrorList

	def as_table(self):
		normal_row = u'''
		%(errors)s
		<tr>
			<td%(html_class_attr)s width="110">
				%(label)s
			</td>
			<td width="225">
				%(field)s
				%(help_text)s
			</td>
		</tr>
		'''
		###
		return self._html_output(
			normal_row = normal_row,
			error_row = u'%s',
			row_ender = u'</td></tr>',
			help_text_html = u'<br /><span class="helptext">%s</span>',
			errors_on_separate_row = False
		)

class AuthorizationForm(BaseAccountForm):

	email = forms.EmailField(label=u'Email', min_length=3, max_length=100, required=True, initial='')
	password = forms.CharField(label="Пароль", widget=forms.PasswordInput, required=True, initial='')

class ForgotForm(BaseAccountForm):

	email = forms.EmailField(label=u'Свой email', min_length=3, max_length=100, required=True, initial='')

	def clean_email(self):
		email = self.cleaned_data['email']
		###
		if len(email) > 100:
			raise forms.ValidationError("Не больше 100 символов")
		###
		if User.objects.filter(email=email).exists():
			return email
		else:
			raise forms.ValidationError("Такой email не существует")

class RegistrationForm(BaseAccountForm):

	email = forms.EmailField(label=u'Email', min_length=3, max_length=100, required=True, initial='')
	name = forms.CharField(label=u'Имя', min_length=3, max_length=100, required=True, initial='')
	address = forms.CharField(label=u'Адрес', min_length=3, max_length=255, required=True, initial='')
	phone = forms.CharField(label=u'Телефон', min_length=3, max_length=100, required=True, initial='')
	password = forms.CharField(label="Пароль", widget=forms.PasswordInput, required=True, initial='')
	confirm = forms.CharField(label="Подтверждение", widget=forms.PasswordInput, required=True, initial='')

	def clean_email(self):
		email = self.cleaned_data['email']
		###
		if len(email) > 100:
			raise forms.ValidationError("Не больше 100 символов")
		###
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Такой email уже используется")
		else:
			return email

	def clean_name(self):
		name = self.cleaned_data['name']
		###
		if not re.compile(ur"^[А-Яа-я\w\s\.\,\-]*$").match(name):
			raise forms.ValidationError(u'Некорректные символы. Допустимы буквы и цифры, а также "-", ",", "."')
		else:
			return name
	
	def clean_address(self):
		address = self.cleaned_data['address']
		###
		if not re.compile(ur"^[А-Яа-я\w\s\.\,\-]*$").match(address):
			raise forms.ValidationError(u'Некорректные символы. Допустимы буквы и цифры, а также "-", ",", "."')
		else:
			return address

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		###
		if not re.compile(r"^[\d\-\(\)\s]*$").match(phone):
			raise forms.ValidationError(u'Некорректные символы. Допустимы "0-9", "-", пробел и "()"')
		else:
			return phone

	def clean_confirm(self):
		p1 = self.cleaned_data.get('password', '')
		p2 = self.cleaned_data['confirm']
		###
		if not p1 == p2:
			raise forms.ValidationError(u'Пароль и подтверждение не совпадают')
		else:
			return p2


class UserProfileForm(forms.ModelForm):

	password = forms.CharField(label="Пароль*", widget=forms.PasswordInput, required=False, initial='')
	confirm = forms.CharField(label="Подтверждение", widget=forms.PasswordInput, required=False, initial='')
	
	class Meta:
		model = UserProfile
		fields = ('name', 'address', 'phone',)

	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		###
		self.error_class = FormErrorList

	def clean_confirm(self):
		p1 = self.cleaned_data.get('password', '')
		p2 = self.cleaned_data['confirm']
		###
		if p1 == '' and p2 == '':
			return p2
		else:
			if not p1 == p2:
				raise forms.ValidationError(u'Пароль и подтверждение не совпадают')
			else:
				return p2

	def clean_name(self):
		name = self.cleaned_data['name']
		###
		if not re.compile(ur"^[А-Яа-я\w\s\.\,\-]*$").match(name):
			raise forms.ValidationError(u'Некорректные символы. Допустимы буквы и цифры, а также "-", ",", "."')
		else:
			return name
	
	def clean_address(self):
		address = self.cleaned_data['address']
		###
		if not re.compile(ur"^[А-Яа-я\w\s\.\,\-]*$").match(address):
			raise forms.ValidationError(u'Некорректные символы. Допустимы буквы и цифры, а также "-", ",", "."')
		else:
			return address

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		###
		if not re.compile(r"^[\d\-\(\)\s]*$").match(phone):
			raise forms.ValidationError(u'Некорректные символы. Допустимы "0-9", "-", пробел и "()"')
		else:
			return phone

	def as_table(self):
		normal_row = u'''
		%(errors)s
		<tr>
			<td%(html_class_attr)s width="110">
				%(label)s
			</td>
			<td width="225">
				%(field)s
				%(help_text)s
			</td>
		</tr>
		'''
		###
		return self._html_output(
			normal_row = normal_row,
			error_row = u'%s',
			row_ender = u'</td></tr>',
			help_text_html = u'<br /><span class="helptext">%s</span>',
			errors_on_separate_row = False
		)
