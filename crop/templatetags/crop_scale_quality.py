# -*- coding: utf-8 -*-
from django import template
from collage.crop.settings import MIN_W, MAX_SIZE

register = template.Library()

def scale_quality(w, h):
	size = w < h and w or h
	###
	if (size >= MAX_SIZE):
		size = MAX_SIZE - int(MAX_SIZE * 0.02)
	###
	return {
		'percent':int((size * 100) / MAX_SIZE),
	}

register.inclusion_tag('templatetags/crop_scale_quality.html')(scale_quality)
