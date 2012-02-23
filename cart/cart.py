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

	def v2d(self, id, t, auth):
		return {'id':int(id), 't':int(t), 'auth':auth}

	def add(self, id=None, t=0, auth=True):
		ok = False
		###
		item = self.v2d(id, t, auth)
		###
		if not self.is_cart(item):
			self.data.append(item)
			###
			ok = True
		###
		return ok

	def delete(self, id=None, t=0, auth=True):
		ok = False
		###
		item = self.v2d(id, t, auth)
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

	def get_data(self, auth=True, t=0):
		data = []
		###
		for item in self.data:
			if (item['auth'] == auth) and (item['t'] == t):
				data.append(item)
		###
		return data

	def reload(self, auth=False):
		for item in self.data:
			if not item['auth'] == auth:
				item['auth'] = auth
