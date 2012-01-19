# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from django.db.models.signals import post_save

GENDER_CHOICES = (
	(u'M', u'Male',),
	(u'F', u'Female',),
)

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True, related_name='profile')
	avatar = models.ImageField(u'Аватар', blank=True, upload_to='avatar/')
	gender = models.CharField(u'Пол', blank=True, null=True, max_length=1, choices=GENDER_CHOICES)
	about = models.CharField(u'О себе', blank=True, null=True, max_length=500)
	auth_key = models.CharField(blank=True, max_length=50)

	def __init__(self, *args, **kwargs):
		super(UserProfile, self).__init__(*args, **kwargs)

def create_user_profile(sender, instance, created, **kwargs):
	if (created and sender.__name__ == 'User'):
		# Обход двойного вызова сигнала. Почему сигнал вызывается два раза - непонятно
		if not UserProfile.objects.filter(user=instance).exists():
			UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class UsersOnline(models.Model):
	username = models.CharField(max_length=30)
	time = models.DateTimeField()
	ip_adress = models.IPAddressField(blank=True, null=True)
