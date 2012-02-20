# -*- coding: utf-8 -*-

from collage.puzzle.settings import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea

class Choises(models.Model):

	name = models.CharField(u'Название', max_length=100, blank=False)
	price = models.FloatField(u'Сумма', blank=False)

	class Meta:
		abstract = True

	def __unicode__(self):
		return u'%s' % self.name

	def preview_image_url(self):
			return '<a href="%s/"><img src="%s%s" style="width: 100px; height: 100px;"/></a>' % (str(self.id), MEDIA_URL, self.img.name)
	###
	preview_image_url.short_description = 'Изображение'
	preview_image_url.allow_tags = True

class Frames(Choises):

	img = models.ImageField(u'Изображение', upload_to='frames/', max_length=150, blank=False)

	class Meta:
		verbose_name = u'Рамки'
		verbose_name_plural = u'Рамки'
		ordering = ['id']

class Packaging(Choises):

	img = models.ImageField(u'Изображение', upload_to='packaging/', max_length=150, blank=False)

	class Meta:
		verbose_name = u'Упаковки'
		verbose_name_plural = u'Упаковки'
		ordering = ['id']

class Stretch(models.Model):

	name = models.CharField(u'Название', max_length=100, blank=False, default='')
	descr = models.CharField(u'Описание', max_length=255, blank=True, default='')
	koef = models.FloatField(u'Коэфициент', blank=False, default=1)
	defrow = models.BooleanField(u'Натяжка по умолчанию', default=False)

	def __unicode__(self):
		return u'%s' % self.name

	class Meta:
		verbose_name = u'Натяжка'
		verbose_name_plural = u'Натяжка'
		ordering = ['id']

	def save(self):
		if self.defrow:
			Stretch.objects.all().update(defrow=False)
		###
		super(Stretch, self).save()
