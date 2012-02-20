# -*- coding: utf-8 -*-
import datetime
from md5 import md5
from collage.common.settings import SECRET_KEY

class GuestId(object):

	days = 14
	days_expire = 1
	cookie_key = 'nouser'
	keyId = None

	def __init__(self, request):
		self.days_expire = self.days * 24 * 60 * 60
		###
		self.get(request)

	def newId(self):
		return md5(''.join([SECRET_KEY[10], str(datetime.datetime.now())])).hexdigest()

	def getExpires(self):
		return datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=self.days_expire), "%a, %d-%b-%Y %H:%M:%S GMT")

	def set(self, response=None):
		response.set_cookie(self.cookie_key, self.keyId, max_age=self.days_expire, expires=self.getExpires())
		###
		return response

	def get(self, request=None):
		if self.keyId is None:
			if request.COOKIES.has_key(self.cookie_key):
				keyId = request.COOKIES[self.cookie_key]
				###
				if not len(keyId) == 32:
					keyId = self.newId()
			else:
				keyId = self.newId()
			###
			self.keyId = keyId
		###
		return self.keyId
			
class NobodyMiddleware(object):

	def process_request(self, request):
		request.NOUSER = GuestId(request)

	def process_response(self, request, response):
		if hasattr(request, 'NOUSER'):
			return request.NOUSER.set(response)
		else:
			return response
