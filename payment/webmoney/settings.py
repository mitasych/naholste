# -*- coding: utf-8 -*-
import os
from django.contrib.sites.models import Site

domain = Site.objects.get_current().name

# Номер платежа в вашей системе (в вашем интернет-магазине)
LMI_PAYMENT_NO = ''

# Номер вашего кошелька в WebMoney, например R12345678900
LMI_PAYEE_PURSE = 'Z326284314133'

# URL вашей страницы, на которую покупатель попадет после оплаты в системе WebMoney в случае успешной операции
LMI_SUCCESS_URL = ''.join(['http://', domain, '/payment/success/'])

# Метод вызова вашей успешной страницы, указанной в LMI_SUCCESS_URL. Варианты: 0 — GET, 1 — POST, 2 — LINK
LMI_SUCCESS_METHOD = '0'

# URL вашей страницы, на которую покупатель попадет в случае ошибки оплаты в системе WebMoney или если покупатель просто отказался от оплаты
LMI_FAIL_URL = ''.join(['http://', domain, '/payment/fail/'])

# Метод вызова вашей страницы в случае ошибки. Варианты такие же: 0 — GET, 1 — POST, 2 — LINK
LMI_FAIL_METHOD = '0'

# URL вашей страницы с обработкой платежа
LMI_RESULT_URL = ''.join(['http://', domain, '/payment/webmoney/'])

# URL webmoney
FORM_ACTION = 'https://merchant.webmoney.ru/lmi/payment.asp'

# Секретный ключ
SECRET_KEY = 'jhff8fkldj'
