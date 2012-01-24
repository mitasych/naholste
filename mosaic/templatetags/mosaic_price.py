# -*- coding: utf-8 -*-

from django import template

register = template.Library()

def mosaic_price(MosaicPrice, row_id):
	ret = ''
	###
	for p in MosaicPrice:
		if p.size_id == row_id:
			ret = p.__unicode__()
			###
			break
	###
	return ret == '' and '' or ''.join([' - (', ret, ')'])

mosaic_price = register.simple_tag(mosaic_price)
