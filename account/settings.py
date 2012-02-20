# -*- coding: utf-8 -*-
import os
from collage.settings import *

PATH_PJT_ACCOUNT = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS += (
	''.join([PATH_PJT_ACCOUNT, '/templates']),
)

EMAIL_FROM = 'aries.ua@gmail.com'
