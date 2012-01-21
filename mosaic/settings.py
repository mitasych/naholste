# -*- coding: utf-8 -*-

import os
from collage.settings import *

PATH_PJT_CROP = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS += (
	''.join([PATH_PJT_CROP, '/templates']),
)

SAVE_IMG_EXT = 'jpg'

FILES_DIR = ''.join([PATH_PJT_CROP, '/../media/files/mosaic/'])

MEDIA_URL_FILES = 'files/mosaic/'

DIR_NOBODY = 'nobody/'
DIR_AUTH = 'auth/'
DIR_THUMBS = 'thumbs/'
DIR_CHANGE = 'change/'
DIR_SMALLTHUMBS = 'smallthumbs/'

MIN_W = 300
MIN_H = 300
MIN_DPI = 72

TYPE_SIZE_1 = (
	(150, 150,),
	(150, 150,),
	(150, 150,),
	(150, 150,),
	(150, 150,),
	(150, 150,),
	(150, 150,),
	(150, 150,),
	(150, 150,),
)

TYPE_SIZE_2 = (
	(288, 192,),
	(192, 144,),
	(144, 192,),
	(144, 192,),
	(96, 96,),
	(96, 96,),
	(192, 144,),
)

TYPE_SIZE_3 = (
	(240, 180,),
	(240, 180,),
	(240, 360,),
	(180, 240,),
	(120, 120,),
	(120, 120,),
	(180, 240,),
)
