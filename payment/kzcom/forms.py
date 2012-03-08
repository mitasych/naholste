# -*- coding: utf-8 -*-

import os
from django import forms
from settings import FORM_LANG, FORM_BACK, FORM_POST

class PayForm(forms.Form):

	Signed_Order_B64 = forms.CharField(widget=forms.HiddenInput(), initial='')
	email = forms.EmailField(label=u'Email', min_length=5, max_length=100, initial='')
	Language = forms.CharField(widget=forms.HiddenInput(), initial=FORM_LANG)
	BackLink = forms.CharField(widget=forms.HiddenInput(), initial=FORM_BACK)
	PostLink = forms.CharField(widget=forms.HiddenInput(), initial=FORM_POST)
