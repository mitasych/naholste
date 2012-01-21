# -*- coding: utf-8 -*-
from collage.settings import *
import os

PATH_PJT_ACCOUNT = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS += (
	''.join([PATH_PJT_ACCOUNT, '/templates']),
)
