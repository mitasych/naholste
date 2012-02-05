# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site

class Cart(object):

	data = []
	domain = ''

	def __init__(self, data):
		self.domain = Site.objects.get_current().name
		###
		if type(data).__name__ == 'list':
			self.data = data

	def v2d(self, opt_id, type_id, reg):
		return {'opt_id':opt_id, 'type_id':type_id, 'reg':reg}

	def set(self, opt_id=None, type_id=0, reg=True):
		add = False
		###
		item = self.v2d(opt_id, type_id, reg)
		###
		if not self.is_cart(item):
			self.data.append(item)
			###
			add = True
		###
		return add

	def delete(self, opt_id=None, type_id=0, reg=True):
		ok = False
		###
		opt_id = type_id == 3 and int(opt_id) or opt_id
		###
		item = self.v2d(opt_id, type_id, reg)
		###
		if self.is_cart(item):
			self.data.remove(item)
			###
			ok = True
		###
		return ok

	def clear(self):
		self.data = []

	def get(self):
		return self.data

	def is_cart(self, item):
		return item in self.data

	def get_data(self, reg=True, type_id=0):
		data = []
		###
		for item in self.data:
			if (item['reg'] == reg) and (item['type_id'] == type_id):
				data.append(item)
		###
		return data

	def reload(self, auth=False):
		for item in self.data:
			if not item['reg'] == auth:
				item['reg'] = auth
