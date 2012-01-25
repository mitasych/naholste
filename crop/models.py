# -*- coding: utf-8 -*-

from settings import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea

STRETCH_CHOISES = (
	(1, u'Стандартная',),
	(2, u'Галерейная',),
	(3, u'Холст',),
)

TYPE_CHOISES = (
	(1, u'Альбомная',),
	(2, u'Книжная',),
	(3, u'Квадрат',),
)

SIZE_CHOISES = (
	(1, u'30x20 см',),
	(2, u'40x30 см',),
	(3, u'50x40 см',),
	(4, u'60x40 см',),
	(5, u'70x50 см',),
	(6, u'90x60 см',),
	(7, u'30x30 см',),
	(8, u'40x40 см',),
	(9, u'50x50 см',),
	(10, u'60x60 см',),
	(11, u'70x70 см',),
	(12, u'90x90 см',),
)

EFFECT_CHOISES = (
	(1, u'Нет',),
	(2, u'Черно-белое',),
	(3, u'Сепия',),
)

class CropPrice(models.Model):

	size_id = models.IntegerField(u'Размер', choices=SIZE_CHOISES, blank=False)
	price = models.DecimalField(u'Цена', max_digits=5, decimal_places=2, blank=False)

	class Meta:
		verbose_name = u'Размеры и цены'
		verbose_name_plural = u'Размеры и цены'

	def __unicode__(self):
		return u'%s тенге' % self.price

class Files(models.Model):

	char_id = models.CharField(u'Строковый ИД', max_length=32)
	user = models.ForeignKey(User)
	ext = models.CharField(u'Расширение', max_length=10)
	pth = models.CharField(u'Путь', max_length=255)

	def __unicode__(self):
		return self.char_id

	def getListCookie(self, cookie=[]):
		data = []
		###
		for f in cookie:
			if os.path.isfile(''.join([FILES_DIR, DIR_NOBODY, f, '.', SAVE_IMG_EXT])):
				data.append({
					'id':'0',
					'char_id':f,
					'user_id':'0',
					'ext':SAVE_IMG_EXT,
					'pth':''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_NOBODY,]),
				})
		###
		return data

	def getRow(self, f=''):
		return {
			'id':'0',
			'char_id':f,
			'user_id':'0',
			'ext':SAVE_IMG_EXT,
			'pth':''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_NOBODY,]),
		}

class Frames(models.Model):
	
	cod = models.CharField(u'Код рамки', max_length=30)
	file_name = models.CharField(u'Имя файла', max_length=255)

	def __unicode__(self):
		return self.cod

class Packaging(models.Model):
	
	cod = models.CharField(u'Код рамки', max_length=30)
	file_name = models.CharField(u'Имя файла', max_length=255)

	def __unicode__(self):
		return self.cod

class OptionFiles(models.Model):

	file = models.ForeignKey(Files)
	img_stretch = models.SmallIntegerField(u'Натяжка', max_length=1)
	img_type = models.SmallIntegerField(u'Тип', max_length=1)
	img_size = models.SmallIntegerField(u'Размеры', max_length=1)
	img_effect = models.SmallIntegerField(u'Эффекты', max_length=1)
	qty = models.IntegerField(u'Количество')
	x1 = models.IntegerField(u'x1')
	y1 = models.IntegerField(u'y1')
	x2 = models.IntegerField(u'x2')
	y2 = models.IntegerField(u'y2')
	frame = models.OneToOneField(Frames, blank=True)
	packaging = models.OneToOneField(Packaging, blank=True)

