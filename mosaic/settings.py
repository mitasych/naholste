# -*- coding: utf-8 -*-

import os
from collage.settings import *

PATH_PJT_MOSAIC = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS += (
	''.join([PATH_PJT_MOSAIC, '/templates']),
)

IMG_EXT = 'jpg'

FILES_DIR = ''.join([PATH_PJT_MOSAIC, '/../media/files/mosaic/'])

MEDIA_URL_FILES = 'files/mosaic/'

DIR_THUMBS = 'thumbs/'
DIR_SMALLTHUMBS = 'smallthumbs/'

MIN_W = 500
MIN_H = 500

if DEBUG:
	MIN_DPI = 72
else:
	MIN_DPI = 150

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

REDIRECT = 'mosaic.views.choise'
