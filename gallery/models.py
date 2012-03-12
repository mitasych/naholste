# -*- coding: utf-8 -*-

from settings import *
from django.contrib.auth.models import User

import mimetypes
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify


class Album(models.Model):
    img = models.ImageField(u'Изображение', upload_to='albums/', max_length=150, blank=False)
    name = models.CharField(u'Название', blank=False, max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name = u'Альбомы'
        verbose_name_plural = u'Альбомы'

    def __unicode__(self):
        return self.name
    
class Images(models.Model):
    album = models.ForeignKey(Album, blank = False)
    img = models.ImageField(u'Изображение', upload_to='gallery/', max_length=150, blank=False)
    name = models.CharField(u'Название', blank=False, max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображение'

    def __unicode__(self):
        return self.name

    def preview_image_url(self):
            return '<a href="%s/"><img src="%s%s" style="width: 100px;"/></a>' % (str(self.id), MEDIA_URL, self.img.name)
    ###
    preview_image_url.short_description = 'Изображение'
    preview_image_url.allow_tags = True