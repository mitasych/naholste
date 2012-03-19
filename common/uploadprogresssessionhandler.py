# -*- coding: utf-8 -*-

from django.core.files.uploadhandler import FileUploadHandler

class UploadProgressSessionHandler(FileUploadHandler):

	def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
		data = {
			'length':content_length,
			'uploaded':0,
			'stop':0,
		}
		###
		self.request.session['progressbar'] = data
		self.request.session.save()

	def receive_data_chunk(self, raw_data, start):
		data = self.request.session.get('progressbar', None)
		###
		if data is not None:
			data['uploaded'] += self.chunk_size
			###
			self.request.session['progressbar'] = data
			self.request.session.save()
		###
		return raw_data

	def file_complete(self, file_size):
		data = self.request.session.get('progressbar', None)
		###
		if data is not None:
			self.request.session['progressbar'] = None
			self.request.session.save()
