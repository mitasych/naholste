# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):

	user = models.ForeignKey(User, unique=True, related_name='profile')
	auth_key = models.CharField(blank=True, max_length=50)
	address = models.CharField(u'Адрес', max_length=255, blank=False, default='')
	name = models.CharField(u'Имя', max_length=255, blank=False, default='')
	phone = models.CharField(u'Телефон', max_length=50, blank=False, default='')
	created = models.DateTimeField(u'Создан', auto_now=True)

	class Meta:
		verbose_name = u'Профиль пользователя'
		verbose_name_plural = u'Профиль пользователя'

	def __init__(self, *args, **kwargs):
		super(UserProfile, self).__init__(*args, **kwargs)

def create_user_profile(sender, instance, created, **kwargs):
	if (created and sender.__name__ == 'User'):
		# Обход двойного вызова сигнала. Почему сигнал вызывается два раза - непонятно
		if not UserProfile.objects.filter(user=instance).exists():
			UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
