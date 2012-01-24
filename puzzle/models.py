# -*- coding: utf-8 -*-

from collage.puzzle.settings import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from collage.crop.models import Frames, Packaging

STRETCH_CHOISES = (
	(1, u'Стандартная',),
	(2, u'Галерейная',),
	(3, u'Холст',),
)

TYPE_CHOISES = (
	(1, u'Альбомная',),
	(2, u'Книжная',),
)

SIZE_CHOISES = (
	(1, u'Нет ',),
	(2, u'4-45x45',),
	(3, u'3-25x100',),
	(4, u'4-30x30',),
	(5, u'3-45x45',),
	(6, u'6-30x30',),
	(7, u'6-45x45',),
	(8, u'5-25x100',),
	(9, u'9-30x30',),
	(10, u'9-45x45',),
	(11, u'3-30x30',),
	(12, u'3-25x50',),
)

EFFECT_CHOISES = (
	(1, u'Нет',),
	(2, u'Черно-белое',),
	(3, u'Сепия',),
)

class PuzzlePrice(models.Model):

	size_id = models.IntegerField(u'Размер', choices=SIZE_CHOISES, blank=False)
	price = models.DecimalField(u'Цена', max_digits=5, decimal_places=2, blank=False)

	class Meta:
		verbose_name = u'Размеры и цены'
		verbose_name_plural = u'Размеры и цены'

	def __unicode__(self):
		return u'%d тенге' % self.price

class PuzzleFiles(models.Model):

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

class PuzzleOption(models.Model):

	file = models.ForeignKey(PuzzleFiles)
	img_stretch = models.SmallIntegerField(u'Натяжка', max_length=1)
	img_type = models.SmallIntegerField(u'Тип', max_length=1)
	img_size = models.SmallIntegerField(u'Размеры', max_length=1)
	img_effect = models.SmallIntegerField(u'Эффекты', max_length=1)
	qty = models.IntegerField(u'Количество')
	frame = models.OneToOneField(Frames, blank=True)
	packaging = models.OneToOneField(Packaging, blank=True)

