# -*- coding: utf-8 -*-

import os
from collage.settings import *

PATH_PJT_CROP = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS += (
	''.join([PATH_PJT_CROP, '/templates']),
)

IMG_EXT = 'jpg'

FILES_DIR = ''.join([PATH_PJT_CROP, '/../media/files/crop/'])

MEDIA_URL_FILES = 'files/crop/'

DIR_THUMBS = 'thumbs/'
DIR_SMALLTHUMBS = 'smallthumbs/'

MIN_W = 500
MIN_H = 500

if DEBUG:
	MIN_DPI = 72
else:
	MIN_DPI = 150

THUMB_W = 500
THUMB_X = 400

MAX_SIZE = 3000
