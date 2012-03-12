# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.core.mail import send_mail
from django.contrib import messages

from collage.contacts.forms import ContactForm

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			phone = form.cleaned_data['phone']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']
			
			recipients = ['info@naholste.kz']
			if cc_myself:
				recipients.append(sender)
				
			message_ok = 'Phone: ' + phone + "\r\n" + message
			
			send_mail(subject, message_ok, sender, recipients)
			
			messages.success(request, 'Ваше сообщение отправлено')
			return HttpResponseRedirect('/contacts/')
	else:
		data = {
			'form':ContactForm(),
		}

	return render(request, 'contact.html', data)
