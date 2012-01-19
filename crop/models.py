# -*- coding: utf-8 -*-

from settings import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea

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

