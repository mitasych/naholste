# -*- coding: utf-8 -*-
from django import template
from collage.crop.settings import MEDIA_URL, MEDIA_URL_FILES, DIR_SMALLTHUMBS, IMG_EXT

register = template.Library()

def list_crop_thumbs(thumbs=[]):
	return {
		'thumbs':thumbs,
		'total_thumbs':len(thumbs),
		'dir':''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_SMALLTHUMBS]),
		'ext':IMG_EXT,
	}

def view_step(current):
	return {'current':current,}

register.inclusion_tag('templatetags/crop_list_thumbs.html')(list_crop_thumbs)
register.inclusion_tag('templatetags/crop_view_step.html')(view_step)
