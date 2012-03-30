# -*- coding: utf-8 -*-

import os
import re
from django import forms

class QiwiForm(forms.Form):

	phone = forms.CharField(label=u'Телефон', min_length=3, max_length=100, required=True, initial='')

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		###
		if not re.compile(r"^[\d\-\(\)\s]*$").match(phone):
			raise forms.ValidationError(u'Некорректные символы. Допустимы "0-9", "-", пробел и "()"')
		else:
			return phone
