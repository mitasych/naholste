# -*- coding: utf-8 -*-
from django import template
from collage.mosaic.context_processors import set_settings
from django.core.context_processors import csrf
from collage.mosaic.models import Mosaic
from collage.mosaic.forms import UploadForm
from collage.mosaic.settings import MEDIA_URL, MEDIA_URL_FILES, DIR_THUMBS, IMG_EXT

register = template.Library()

def mosaic_table(context, inst):
	request = context['request']
	###
	param = set_settings(request)
	###
	param['thumb'] = inst
	param['dir'] = ''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_THUMBS])
	param['ext'] = IMG_EXT
	###
	return param

def mosaic_table_1(context, inst):
	return mosaic_table(context, inst)

def mosaic_table_2(context, inst):
	return mosaic_table(context, inst)

def mosaic_table_3(context, inst):
	return mosaic_table(context, inst)

def mosaic_table_form(context=[], thumb={}, div_id=0, width=0):
	initial = {
		'div_id':div_id,
		'effect':thumb.img_effect,	
	}
	###
	return {
		'id':thumb.id,
		'form':UploadForm(initial),
		'div_id':div_id,
		'width':width,
		'request':context,
	}

register.inclusion_tag('templatetags/mosaic_table_1.html', takes_context=True)(mosaic_table_1)
register.inclusion_tag('templatetags/mosaic_table_2.html', takes_context=True)(mosaic_table_2)
register.inclusion_tag('templatetags/mosaic_table_3.html', takes_context=True)(mosaic_table_3)
register.inclusion_tag('templatetags/mosaic_table_form.html', takes_context=True)(mosaic_table_form)
