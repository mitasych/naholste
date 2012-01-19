# -*- coding: utf-8 -*-
from django import template
from collage.crop.settings import DIR_SMALLTHUMBS
from collage.common.helpers import CookieListFiles
from collage.crop.models import Files

register = template.Library()

def list_thumbs(thumbs=[]):
	return {
		'thumbs':thumbs,
		'total_thumbs':len(thumbs),
		'dir_smallthumbs':DIR_SMALLTHUMBS,
	}

def view_mess_cook(context):
	request = context['request']
	user = request.user
	###
	ret = {'view_cook':False,}
	###
	if (user.is_authenticated() and user.is_active):
		data = CookieListFiles().get_data(request)
		###
		ret['view_cook'] = len(Files().getListCookie(data)) > 0
	###
	return ret

def view_step(current):
	return {'current':current,}

register.inclusion_tag('templatetags/crop_list_thumbs.html')(list_thumbs)
register.inclusion_tag('templatetags/view_mess_cook.html', takes_context=True)(view_mess_cook)
register.inclusion_tag('templatetags/crop_view_step.html')(view_step)
