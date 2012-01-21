# -*- coding: utf-8 -*-

import os
from collage.settings import *

PATH_PJT_CROP = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS += (
	''.join([PATH_PJT_CROP, '/templates']),
)

SAVE_IMG_EXT = 'jpg'

FILES_DIR = ''.join([PATH_PJT_CROP, '/../media/files/'])

MEDIA_URL_FILES = 'files/'

DIR_NOBODY = 'nobody/'
DIR_AUTH = 'auth/'
DIR_THUMBS = 'thumbs/'
DIR_CHANGE = 'change/'
DIR_SMALLTHUMBS = 'smallthumbs/'

MIN_W = 500
MIN_H = 500
MIN_DPI = 300

THUMB_W = 500
THUMB_X = 400

MAX_SIZE = 3000