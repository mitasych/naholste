# -*- coding: utf-8 -*-

from settings import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from collage.common.models import Frames, Packaging

TYPE_CHOISES = (
	(1, u'Квадрат',),
	(2, u'Альбомная',),
	(3, u'Книжная',),
)

EFFECT_CHOISES = (
	(1, u'Нет',),
	(2, u'Черно-белое',),
	(3, u'Сепия',),
)

class MosaicSize(models.Model):

	name = models.CharField(u'Название', max_length=100, blank=False)
	price = models.FloatField(u'Сумма', blank=False)
	width = models.IntegerField(u'Ширина', blank=False)
	height = models.IntegerField(u'Высота', blank=False)
	defsize = models.BooleanField(u'Размер по умолчанию', default=False)

	def __unicode__(self):
		return u'%s' % self.name

	class Meta:
		verbose_name = u'Список размеров и цен'
		verbose_name_plural = u'Список размеров и цен'
		ordering = ['id']

	def save(self):
		if self.defsize:
			MosaicSize.objects.all().update(defsize=False)
		###
		super(MosaicSize, self).save()

class Mosaic(models.Model):

	user = models.ForeignKey(User, blank=True, null=True, verbose_name=u'Пользователь')
	nouser = models.CharField(u'Гость', blank=True, default='', max_length=32)
	table_type = models.IntegerField(u'Тип', choices=TYPE_CHOISES, blank=True, default=1)
	img_size = models.ForeignKey(MosaicSize, blank=True, null=True, verbose_name=u'Размер')
	img_effect = models.SmallIntegerField(u'Эффекты', blank=False, max_length=1, choices=EFFECT_CHOISES)
	qty = models.IntegerField(u'Количество')
	frame = models.ForeignKey(Frames, blank=True, null=True)
	packaging = models.ForeignKey(Packaging, blank=True, null=True)
	f_0 = models.CharField(u'Изображение 0', max_length=32, blank=True, default='')
	f_1 = models.CharField(u'Изображение 1', max_length=32, blank=True, default='')
	f_2 = models.CharField(u'Изображение 2', max_length=32, blank=True, default='')
	f_3 = models.CharField(u'Изображение 3', max_length=32, blank=True, default='')
	f_4 = models.CharField(u'Изображение 4', max_length=32, blank=True, default='')
	f_5 = models.CharField(u'Изображение 5', max_length=32, blank=True, default='')
	f_6 = models.CharField(u'Изображение 6', max_length=32, blank=True, default='')
	f_7 = models.CharField(u'Изображение 7', max_length=32, blank=True, default='')
	f_8 = models.CharField(u'Изображение 8', max_length=32, blank=True, default='')
	created = models.DateTimeField(u'Создан', auto_now=True)
