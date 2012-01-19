# -*- coding: utf-8 -*-
from django import template
from collage.puzzle.settings import DIR_SMALLTHUMBS
from collage.common.helpers import CookiePuzzleFiles
from collage.puzzle.models import PuzzleFiles

register = template.Library()

def list_puzzle_thumbs(thumbs=[]):
	return {
		'thumbs':thumbs,
		'total_thumbs':len(thumbs),
		'dir_smallthumbs':DIR_SMALLTHUMBS,
	}

def view_mess_cook_puzzle(context):
	request = context['request']
	user = request.user
	###
	ret = {'view_cook':False,}
	###
	if (user.is_authenticated() and user.is_active):
		data = CookiePuzzleFiles().get_data(request)
		###
		ret['view_cook'] = len(PuzzleFiles().getListCookie(data)) > 0
	###
	return ret

def view_step(current):
	return {'current':current,}

register.inclusion_tag('templatetags/puzzle_list_thumbs.html')(list_puzzle_thumbs)
register.inclusion_tag('templatetags/puzzle_view_mess_cook.html', takes_context=True)(view_mess_cook_puzzle)
register.inclusion_tag('templatetags/puzzle_view_step.html')(view_step)
