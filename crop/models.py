# -*- coding: utf-8 -*-

from settings import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from collage.common.models import Frames, Packaging, Stretch

TYPE_CHOISES = (
	(1, u'Альбомная',),
	(2, u'Книжная',),
	(3, u'Квадрат',),
)

EFFECT_CHOISES = (
	(1, u'Нет',),
	(2, u'Черно-белое',),
	(3, u'Сепия',),
)

class CropSize(models.Model):

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
			CropSize.objects.all().update(defsize=False)
		###
		super(CropSize, self).save()

class Crop(models.Model):

	user = models.ForeignKey(User, blank=True, null=True, verbose_name=u'Пользователь')
	nouser = models.CharField(u'Гость', blank=True, default='', max_length=32)
	img = models.CharField(u'Изображение', max_length=32)
	img_stretch = models.ForeignKey(Stretch, verbose_name=u'Натяжка', blank=False)
	img_type = models.SmallIntegerField(u'Тип', max_length=1, choices=TYPE_CHOISES)
	img_size = models.ForeignKey(CropSize, blank=True, null=True, verbose_name=u'Размер')
	img_effect = models.SmallIntegerField(u'Эффекты', blank=False, max_length=1, choices=EFFECT_CHOISES)
	qty = models.IntegerField(u'Количество')
	frame = models.ForeignKey(Frames, blank=True, null=True)
	packaging = models.ForeignKey(Packaging, blank=True, null=True)
	x1 = models.IntegerField(u'Координата X1', blank=False)
	y1 = models.IntegerField(u'Координата Y1', blank=False)
	x2 = models.IntegerField(u'Координата X2', blank=False)
	y2 = models.IntegerField(u'Координата Y2', blank=False)
	status = models.BooleanField(u'Статус', default=False)
	created = models.DateTimeField(u'Создан', auto_now=True)

