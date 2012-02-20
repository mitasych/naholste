# -*- coding: utf-8 -*-
from django import template
from collage.mosaic.settings import MEDIA_URL, MEDIA_URL_FILES, DIR_SMALLTHUMBS, IMG_EXT

register = template.Library()

def list_mosaic_thumbs(thumbs=[]):
	new = []
	###
	for t in thumbs:
		r = {'id':t.id, 'img':'no'}
		###
		for i in xrange(9):
			v = getattr(t, 'f_%s' % i)
			###
			if not v == '':
				r['img'] = v
				###
				break
		###
		new.append(r)
	###
	return {
		'thumbs':new,
		'total_thumbs':len(new),
		'dir':''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_SMALLTHUMBS]),
		'ext':IMG_EXT,
	}

register.inclusion_tag('templatetags/list_mosaic_thumbs.html')(list_mosaic_thumbs)
