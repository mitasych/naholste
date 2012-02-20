# -*- coding: utf-8 -*-

from collage.puzzle.settings import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from collage.common.models import Frames, Packaging, Stretch

EFFECT_CHOISES = (
	(1, u'Нет',),
	(2, u'Черно-белое',),
	(3, u'Сепия',),
)

class PuzzleSize(models.Model):

	name = models.CharField(u'Название', max_length=100, blank=False)
	img = models.ImageField(u'Изображение', upload_to='puzzle_size/', max_length=150, blank=False)
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
			PuzzleSize.objects.all().update(defsize=False)
		###
		super(PuzzleSize, self).save()

	def preview_image_url(self):
		return '<a href="%s/"><img src="%s%s"/></a>' % (str(self.id), MEDIA_URL, self.img.name)
	###
	preview_image_url.short_description = 'Изображение'
	preview_image_url.allow_tags = True

class Puzzle(models.Model):

	user = models.ForeignKey(User, blank=True, null=True, verbose_name=u'Пользователь')
	nouser = models.CharField(u'Гость', blank=True, default='', max_length=32)
	img = models.CharField(u'Изображение', max_length=32)
	img_stretch = models.ForeignKey(Stretch, verbose_name=u'Натяжка', blank=False)
	img_size = models.ForeignKey(PuzzleSize, blank=True, null=True, verbose_name=u'Размер')
	img_effect = models.SmallIntegerField(u'Эффекты', blank=False, max_length=1, choices=EFFECT_CHOISES)
	qty = models.IntegerField(u'Количество', blank=False)
	frame = models.ForeignKey(Frames, blank=True, null=True)
	packaging = models.ForeignKey(Packaging, blank=True, null=True)
	x1 = models.IntegerField(u'Координата X1', blank=False)
	y1 = models.IntegerField(u'Координата Y1', blank=False)
	x2 = models.IntegerField(u'Координата X2', blank=False)
	y2 = models.IntegerField(u'Координата Y2', blank=False)
	created = models.DateTimeField(u'Создан', auto_now=True)
