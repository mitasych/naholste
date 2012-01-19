# -*- coding: utf-8 -*-
import datetime
import math
from django import template

register = template.Library()

class Pagins(object):

	cfg = {
		'current_page':1,
		'total_pages':0,
		'total_items':0,
		'items_per_page':20,
		'first_page_in_url':False,
		'count_out':3,
		'count_in':5,
		'current_first_item':0,
		'current_last_item':0,
		'previous_page':True,
		'next_page':True,
		'first_page':True,
		'last_page':True,
		'offset':1,
		'base_url':'page=%s&limit=%s',
		'url':'',
	}

	def __init__(self, request=None, config={}):
		self.config = config
		###
		self.request = request

	def setUrl(self):
		try:
			url = self.config['url']
		except:
			url = ''.join(['http://', self.request.META.get('HTTP_HOST', '/'), self.request.META.get('PATH_INFO', ''),])
			###
			if url[-1] != '/':
				url = ''.join([url, '/',])
			###
			if (url.count('?') > 0):
				mark = '&'
			else:
				mark = '?'
			###
			url = ''.join([url, mark, self.cfg['base_url'],])
		###
		self.cfg['url'] = url

	def currentPage(self):
		try:
			self.cfg['current_page'] = self.config['current_page']
		except:
			self.cfg['current_page'] = int(self.request.GET.get('page', self.cfg['current_page']))

	def limitRow(self):
		try:
			self.cfg['items_per_page'] = self.config['items_per_page']
		except:
			self.cfg['items_per_page'] = int(self.request.GET.get('limit', self.cfg['items_per_page']))

	def setVal(self, key):
		try:
			self.cfg[key] = self.config[key]
		except:
			pass

	def getLinks(self):
		n1 = 1
		n2 = min(self.cfg['count_out'], self.cfg['total_pages'])
		###
		n7 = max(1, self.cfg['total_pages'] - self.cfg['count_out'] + 1)
		n8 = self.cfg['total_pages']
		###
		n4 = max(n2 + 1, self.cfg['current_page'] - self.cfg['count_in'])
		n5 = min(n7 - 1, self.cfg['current_page'] + self.cfg['count_in'])
		use_middle = (n5 >= n4)
		###
		n3 = int((n2 + n4) / 2)
		use_n3 = (use_middle and ((n4 - n2) > 1))
		###
		n6 = int((n5 + n7) / 2)
		use_n6 = (use_middle and ((n7 - n5) > 1))
		###
		links = [];
		###
		i = n1
		while (i <= n2):
			links.append({'key':i, 'val':i})
			###
			i = i + 1
		###
		if use_n3:
			links.append({'key':n3, 'val':'&hellip;'})
		###
		i = n4
		while (i <= n5):
			links.append({'key':i, 'val':i})
			###
			i = i + 1
		###
		if use_n6:
			links.append({'key':n6, 'val':'&hellip;'})
		###
		i = n7
		while (i <= n8):
			links.append({'key':i, 'val':i})
			###
			i = i + 1
		###
		return links

	def data(self):
		for k, v in self.cfg.items():
			self.setVal(k)
		###
		self.currentPage()
		self.limitRow()
		self.setUrl()
		###
		self.cfg['total_pages'] = int(math.ceil(self.cfg['total_items'] / self.cfg['items_per_page']))
		self.cfg['current_page'] = int(min(max(1, self.cfg['current_page']), max(1, self.cfg['total_pages'])))
		self.cfg['current_first_item'] = int(min(((self.cfg['current_page'] - 1) * self.cfg['items_per_page']) + 1, self.cfg['total_items']))
		self.cfg['current_last_item'] = int(min(self.cfg['current_first_item'] + self.cfg['items_per_page'] - 1, self.cfg['total_items']))
		###
		if (self.cfg['current_page'] > 1):
			self.cfg['previous_page'] = self.cfg['current_page'] - 1
		else:
			self.cfg['previous_page'] = False
		###
		if (self.cfg['current_page'] < self.cfg['total_pages']):
			self.cfg['next_page'] = self.cfg['current_page'] + 1
		else:
			self.cfg['next_page'] = False
		###
		if (self.cfg['current_page'] == 1):
			self.cfg['first_page'] = False
		else:
			self.cfg['first_page'] = 1
		###
		if (self.cfg['current_page'] >= self.cfg['total_pages']):
			self.cfg['last_page'] = False
		else:
			self.cfg['last_page'] = self.cfg['total_pages']
		###
		self.cfg['offset'] = int(((self.cfg['current_page'] - 1) * self.cfg['items_per_page']))
		###
		self.cfg['links'] = self.getLinks()
		###
		return self.cfg

def render_url(cfg, page):
	return {'url': cfg['url'] % (page, cfg['items_per_page'],),}

def paginator(context, config={}):
	'''
	ИСПОЛЬЗОВАНИЕ В ШАБЛОНЕ
	{% load pagins %} - Подгружаем таг на страницу
	{% paginator pagin_config %} - Показываем сформированный пагинатор
	параметром передается словарь настроек

	ОСНОВНЫЕ ПАРАМЕТРЫ КОНФИГА
	current_page - текущая страница
	total_items - количество строк в выборке
	url - урл для вставки. Обязательно должен иметь два параметра для подстановки
	1. %s - страница перехода, к примеру http://domain.com/index.html?page=%s
	2. %s - лимит строк на странице. (20 по деф.) http://domain.com/index.html?page=%s&limit=%s
	Если не передаете урл. То берется текущий Урл и ему подставляется базовый шаблон
	Базовый шаблон имеет вид page=%s&limit=%s
	'''
	###
	return {'cfg': Pagins(request=context['request'], config=config).data(),}

register.inclusion_tag('templatetags/pagins.html', takes_context=True)(paginator)
register.inclusion_tag('templatetags/render_url.html')(render_url)
