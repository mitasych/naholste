# -*- coding: utf-8 -*-
import re

from settings import *
from django import forms
from django.forms.util import ErrorList
from django.core.exceptions import ValidationError
from django.forms.widgets import RadioSelect

from collage.account.forms import AuthorizationForm
from collage.cart.models import Shiping

SHIPING_CHOICE = tuple((s.id, u'%s - %.02f тенге' % (s.name, s.price)) for s in Shiping.objects.all())

def valid_phone(val):
	if not re.compile(r"^[\d\-\(\)\s]*$").match(val):
		raise ValidationError(u'Некорректные символы. Допустимы "0-9", "-", пробел и "()"')

def valid_text(val):
	if not re.compile(ur"^[А-Яа-я\w\s\.\,\-]*$").match(val):
		raise ValidationError(u'Некорректные символы. Допустимы буквы и цифры, а также "-", ",", "."')

class OrderForm(forms.Form):

	address = forms.CharField(label=u'Адрес доставки', validators=[valid_text], min_length=3, max_length=255, required=True, initial='')
	email = forms.EmailField(label=u'Емаил', min_length=3, max_length=100, required=True, initial='')
	name = forms.CharField(label=u'Имя', validators=[valid_text], min_length=3, max_length=100, required=True, initial='')
	phone = forms.CharField(label=u'Телефон', validators=[valid_phone], min_length=3, max_length=100, required=True, initial='')

	def as_table(self):
		normal_row = u'''
		<tr>
			<td%(html_class_attr)s width="25%%">
				<span class="required">*</span>%(label)s
			</td>
			<td width="75%%">
				%(errors)s
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

class AuthCartForm(AuthorizationForm):

	def as_table(self):
		normal_row = u'''
		<tr>
			<td%(html_class_attr)s width="35%%">
				%(label)s
			</td>
			<td width="65%%">
				%(errors)s
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
	
class ShipingForm(forms.Form):

	shiping = forms.ChoiceField(label='', widget=RadioSelect(), required=True, choices=SHIPING_CHOICE)
