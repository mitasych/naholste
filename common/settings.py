# -*- coding: utf-8 -*-
from collage.settings import *
import os

PATH_PJT_COMMON = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS += (
	''.join([PATH_PJT_COMMON, '/templates']),
)
