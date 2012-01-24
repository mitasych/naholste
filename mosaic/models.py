# -*- coding: utf-8 -*-

from collage.mosaic.settings import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from django.db.models import Max
from collage.crop.models import Frames, Packaging

EFFECT_CHOISES = (
	(1, u'Нет',),
	(2, u'Черно-белое',),
	(3, u'Сепия',),
)

SIZE_CHOISES = (
	(12, 12,),
	(20, 20,),
	(30, 30,),
	(36, 36,),
	(16, 12,),
	(20, 16,),
	(30, 24,),
	(35, 28,),
	(12, 16,),
	(16, 20,),
	(24, 30,),
	(28, 35,),
)

class ChoiseAdmin(object):

	start = 0
	
	def new(self, row):
		self.start = self.start + 1
		###
		return (self.start, u"%sx%s см" % (row[0], row[1]))

ca = ChoiseAdmin()

SIZE_CHOISES_ADMIN = tuple(ca.new(v) for v in SIZE_CHOISES)
	
class MosaicPrice(models.Model):

	size_id = models.IntegerField(u'Размер', choices=SIZE_CHOISES_ADMIN, blank=False)
	price = models.DecimalField(u'Цена', max_digits=5, decimal_places=2, blank=False)

	class Meta:
		verbose_name = u'Размеры и цены'
		verbose_name_plural = u'Размеры и цены'

	def __unicode__(self):
		return u'%d тенге' % self.price

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
