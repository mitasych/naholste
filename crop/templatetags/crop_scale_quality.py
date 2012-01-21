# -*- coding: utf-8 -*-
from django import template
from collage.crop.settings import MIN_W, MAX_SIZE

register = template.Library()

def scale_quality(w, h):
	size = w < h and w or h
	###
	return {
		'percent':int((size * 100) / (MAX_SIZE - MIN_W)),
	}

register.inclusion_tag('templatetags/crop_scale_quality.html')(scale_quality)
