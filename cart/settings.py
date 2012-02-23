# -*- coding: utf-8 -*-

import os
from collage.settings import *

PATH_PJT_CART = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS += (
	''.join([PATH_PJT_CART, '/templates']),
)

EMAILS_LIST = [
	'aries.ua@gmail.com',
]

EMAIL_FROM = 'aries.ua@gmail.com'

ORDERS_DIR = ''.join([PATH_PJT_CART, '/../media/orders'])

MEDIA_URL_ORDERS = 'orders/'
