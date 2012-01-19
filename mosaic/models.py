# -*- coding: utf-8 -*-

from collage.mosaic.settings import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from django.db.models import Max
from collage.crop.models import Frames, Packaging

class MosaicOption(models.Model):

	opt_id = models.IntegerField(u'Идентификатор строки')
	user = models.ForeignKey(User)
	ext = models.CharField(u'Расширение', max_length=10, blank=True, default='')
	pth = models.CharField(u'Путь', max_length=255, blank=True, default='')
	qty = models.IntegerField(u'Количество', blank=True, default=1)
	table_type = models.IntegerField(u'Количество', blank=True, default=1)
	table_size = models.IntegerField(u'Размер', blank=True, default=1)
	effect = models.SmallIntegerField(u'Эффекты', max_length=1)
	frame = models.OneToOneField(Frames, blank=True)
	packaging = models.OneToOneField(Packaging, blank=True)
	f_0 = models.CharField(u'Изображение 0', max_length=32, blank=True, default='')
	f_1 = models.CharField(u'Изображение 1', max_length=32, blank=True, default='')
	f_2 = models.CharField(u'Изображение 2', max_length=32, blank=True, default='')
	f_3 = models.CharField(u'Изображение 3', max_length=32, blank=True, default='')
	f_4 = models.CharField(u'Изображение 4', max_length=32, blank=True, default='')
	f_5 = models.CharField(u'Изображение 5', max_length=32, blank=True, default='')
	f_6 = models.CharField(u'Изображение 6', max_length=32, blank=True, default='')
	f_7 = models.CharField(u'Изображение 7', max_length=32, blank=True, default='')
	f_8 = models.CharField(u'Изображение 8', max_length=32, blank=True, default='')

	def newId(self, user):
		row = MosaicOption.objects.filter(user=user.id).aggregate(Max('opt_id'))
		###
		if row['opt_id__max'] is None:
			new_id = 1
		else:
			new_id = row['opt_id__max'] + 1
		###
		return new_id
