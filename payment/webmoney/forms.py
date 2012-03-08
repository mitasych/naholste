# -*- coding: utf-8 -*-

import os
from django import forms
from settings import *

class PayForm(forms.Form):

	LMI_PAYMENT_AMOUNT = forms.CharField(widget=forms.HiddenInput(), initial=0)
	LMI_PAYMENT_DESC = forms.CharField(widget=forms.HiddenInput(), initial='')
	LMI_PAYMENT_NO = forms.CharField(widget=forms.HiddenInput(), initial='')
	LMI_PAYEE_PURSE = forms.CharField(widget=forms.HiddenInput(), initial=LMI_PAYEE_PURSE)
	LMI_SUCCESS_URL = forms.CharField(widget=forms.HiddenInput(), initial=LMI_SUCCESS_URL)
	LMI_SUCCESS_METHOD = forms.CharField(widget=forms.HiddenInput(), initial=LMI_SUCCESS_METHOD)
	LMI_FAIL_URL = forms.CharField(widget=forms.HiddenInput(), initial=LMI_FAIL_URL)
	LMI_FAIL_METHOD = forms.CharField(widget=forms.HiddenInput(), initial=LMI_FAIL_METHOD)
