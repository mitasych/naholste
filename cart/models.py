# -*- coding: utf-8 -*-

from collage.mosaic.settings import *
from django.db import models
from django.contrib.auth.models import User
from collage.common.models import Frames, Packaging

TYPE_CHOICES = (
	(1, u'На холсте'),
	(2, u'Мультихолст'),
	(3, u'Коллаж'),
)

class Order(models.Model):

	user = models.ForeignKey(User, blank=True, null=True, verbose_name=u'Пользователь')
	nouser = models.CharField(u'Гость', blank=True, default='', max_length=32)
	price = models.FloatField(u'Общая сумма', blank=False, editable=False, default=0)
	shiping_price = models.FloatField(u'Доставка', blank=False, editable=False, default=0)
	address = models.CharField(u'Адрес доставки', max_length=255, blank=False, default='', editable=False)
	email = models.EmailField(u'Емаил', max_length=100, blank=False, editable=False)
	name = models.CharField(u'Имя', max_length=255, blank=False, default='', editable=False)
	phone = models.CharField(u'Телефон', max_length=50, blank=False, default='', editable=False)
	created = models.DateTimeField(u'Создан', auto_now=True, editable=False)

	class Meta:
		verbose_name = u'Список заказов'
		verbose_name_plural = u'Список заказов'

	def __unicode__(self):
		return u'№%s' % (self.id,)

class OrderOption(models.Model):

	order = models.ForeignKey(Order, verbose_name=u'Заказ')
	type_id = models.IntegerField(u'Вид', choices=TYPE_CHOICES, blank=False, editable=False)
	price = models.FloatField(u'Общая сумма', blank=False, editable=False)
	img = models.CharField(u'Изображение', max_length=32, blank=True, default='', editable=False)
	f_0 = models.CharField(u'Изображение 0', max_length=32, blank=True, default='', editable=False)
	f_1 = models.CharField(u'Изображение 1', max_length=32, blank=True, default='', editable=False)
	f_2 = models.CharField(u'Изображение 2', max_length=32, blank=True, default='', editable=False)
	f_3 = models.CharField(u'Изображение 3', max_length=32, blank=True, default='', editable=False)
	f_4 = models.CharField(u'Изображение 4', max_length=32, blank=True, default='', editable=False)
	f_5 = models.CharField(u'Изображение 5', max_length=32, blank=True, default='', editable=False)
	f_6 = models.CharField(u'Изображение 6', max_length=32, blank=True, default='', editable=False)
	f_7 = models.CharField(u'Изображение 7', max_length=32, blank=True, default='', editable=False)
	f_8 = models.CharField(u'Изображение 8', max_length=32, blank=True, default='', editable=False)
	options = models.TextField(u'Опции', blank=False, default='', editable=False)

	class Meta:
		verbose_name = u'Опции заказа'
		verbose_name_plural = u'Опции заказа'

	def __unicode__(self):
		return self.options
