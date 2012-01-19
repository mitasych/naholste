# -*- coding: utf-8 -*-

from collage.mosaic.settings import *

def set_settings(request):
	return {
		'TYPE_SIZE_1':TYPE_SIZE_1,
		'TYPE_SIZE_2':TYPE_SIZE_2,
		'TYPE_SIZE_3':TYPE_SIZE_3,
		###
		'MEDIA_URL_FILES':MEDIA_URL_FILES,
		###
		'DIR_NOBODY':DIR_NOBODY,
		'DIR_AUTH':DIR_AUTH,
		'DIR_THUMBS':DIR_THUMBS,
		'DIR_CHANGE':DIR_CHANGE,
		'DIR_SMALLTHUMBS':DIR_SMALLTHUMBS,
	}
