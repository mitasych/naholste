# -*- coding: utf-8 -*-
import os
from django.contrib.sites.models import Site

domain = Site.objects.get_current().name

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PEM = '/pem'
XML = '/xml'

FORM_ACTION = 'https://epay.kkb.kz/jsp/process/logon.jsp'
FORM_LANG = 'rus'
FORM_BACK = ''.join(['http://', domain, '/cart/show/'])
FORM_POST = ''.join(['http://', domain, '/payment/kzcom/notify/'])

#Серийный номер сертификата Cert Serial Number
MERCHANT_CERTIFICATE_ID = "00C182B189"

#Название магазина (продавца) Shop/merchant Name
MERCHANT_NAME = "Test shop"

#Путь к закрытому ключу Private cert path
PRIVATE_KEY_FN = ''.join([ROOT_DIR, PEM, '/test_prv.pem'])

#Пароль к закрытому ключу Private cert password
PRIVATE_KEY_PASS = "nissan"

#Путь к XML шаблону XML template path
XML_TEMPLATE_FN = ''.join([ROOT_DIR, XML, '/template.xml'])

#Путь к XML шаблону для команд (возврат/подтверждение)
XML_COMMAND_TEMPLATE_FN = ''.join([ROOT_DIR, XML, '/command_template.xml'])

#Путь к открытому ключу Public cert path
PUBLIC_KEY_FN = ''.join([ROOT_DIR, PEM, '/kkbca.pem'])

#Терминал ИД в банковской Системе
MERCHANT_ID = "92061101"
