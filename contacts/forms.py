# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=100, required=False)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
