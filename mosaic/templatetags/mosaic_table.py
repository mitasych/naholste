# -*- coding: utf-8 -*-
from django import template
from collage.mosaic.context_processors import set_settings
from django.core.context_processors import csrf
from collage.mosaic.forms import MosaicUploadForm, MosaicOptionForm

register = template.Library()

def mosaic_table_1(context, row):
	request = context['request']
	###
	param = set_settings(request)
	###
	param['row'] = row
	###
	return param

def mosaic_table_2(context, row):
	request = context['request']
	###
	param = set_settings(request)
	###
	param['row'] = row
	###
	return param

def mosaic_table_3(context, row):
	request = context['request']
	###
	param = set_settings(request)
	###
	param['row'] = row
	###
	return param

def mosaic_table_form(context=[], row={}, div=0, width=0):
	row['div_id'] = div
	row['img_effect'] = row['effect']
	###
	return {
		'form':MosaicUploadForm(row),
		'div_id':div,
		'width':width,
		'row':row,
		'request':context,
	}

def mosaic_thumbs(context=[], thumbs=[]):
	request = context['request']
	###
	if not type(thumbs).__name__ == 'list':
		form = MosaicOptionForm()
		###
		_t = []
		###
		for i in thumbs:
			_t.append(form.getDataRow(i))
		###
		thumbs = _t
	###
	for t in thumbs:
		t['f_smallthumb'] = ''
		###
		for i in xrange(9):
			if not t['f_%s' % (i,)] == '':
				t['f_smallthumb'] = t['f_%s' % (i,)]
				###
				break
	###
	param = set_settings(request)
	###
	param['thumbs'] = thumbs
	param['total_thumbs'] = len(thumbs)
	###
	return param

register.inclusion_tag('templatetags/mosaic_table_1.html', takes_context=True)(mosaic_table_1)
register.inclusion_tag('templatetags/mosaic_table_2.html', takes_context=True)(mosaic_table_2)
register.inclusion_tag('templatetags/mosaic_table_3.html', takes_context=True)(mosaic_table_3)
register.inclusion_tag('templatetags/mosaic_table_form.html', takes_context=True)(mosaic_table_form)
register.inclusion_tag('templatetags/mosaic_list_thumbs.html', takes_context=True)(mosaic_thumbs)
