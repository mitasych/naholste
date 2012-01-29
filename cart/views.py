# -*- coding: utf-8 -*-

from collage.cart.settings import *
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, HttpResponseBadRequest
from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from collage.common.helpers import CookieListOptions, CookiePuzzleOption, CookieMosaicOption

from collage.crop.models import CropPrice, Files, OptionFiles, Frames, Packaging
from collage.crop.forms import OptionForm

from collage.puzzle.models import PuzzlePrice, PuzzleFiles, PuzzleOption
from collage.puzzle.forms import OptionForm as PuzzleForm

from collage.mosaic.models import MosaicPrice, MosaicOption
from collage.mosaic.forms import MosaicOptionForm

class Id2Name(object):

	user = None

	def set(self):
		pass

	def auth(self):
		pass

	def nobody(self):
		pass

	def get(self):
		if (self.user.is_authenticated() and self.user.is_active):
			return self.auth()
		else:
			return self.nobody()

	def i2n(self, id, tpl):
		name = ''
		###
		for i in tpl:
			if id == i[0]:
				name = i[1]
				###
				break
		###
		return name

class CropId2Name(Id2Name):

	def __init__(self):
		from collage.crop.settings import MEDIA_URL, SAVE_IMG_EXT, MEDIA_URL_FILES, DIR_NOBODY, DIR_AUTH, DIR_SMALLTHUMBS
		from collage.crop.models import STRETCH_CHOISES, TYPE_CHOISES, SIZE_CHOISES, EFFECT_CHOISES
		###
		self.STRETCH_CHOISES = STRETCH_CHOISES
		self.TYPE_CHOISES = TYPE_CHOISES
		self.SIZE_CHOISES = SIZE_CHOISES
		self.EFFECT_CHOISES = EFFECT_CHOISES
		###
		self.SAVE_IMG_EXT = SAVE_IMG_EXT
		self.MEDIA_URL = MEDIA_URL
		self.MEDIA_URL_FILES = MEDIA_URL_FILES
		self.DIR_NOBODY = DIR_NOBODY
		self.DIR_AUTH = DIR_AUTH
		self.DIR_SMALLTHUMBS = DIR_SMALLTHUMBS

	def set(self, row, auth=False):
		row['price'] = CropPrice.objects.get(size_id=row['img_size']).price
		row['summ'] = float(row['price']) * float(row['qty'])
		###
		row['image'] = self.image(row['pth'], row['char_id'], auth)
		###
		row['img_stretch'] = self.i2n(int(row['img_stretch']), self.STRETCH_CHOISES)
		row['img_type'] = self.i2n(int(row['img_type']), self.TYPE_CHOISES)
		row['img_size'] = self.i2n(int(row['img_size']), self.SIZE_CHOISES)
		row['img_effect'] = self.i2n(int(row['img_effect']), self.EFFECT_CHOISES)
		###
		return row

	def image(self, pth=None, char_id='', auth=False):
		url = ''
		###
		if auth:
			url = ''.join([pth, self.DIR_SMALLTHUMBS, char_id, '.', self.SAVE_IMG_EXT])
		else:
			url = ''.join([self.MEDIA_URL, self.MEDIA_URL_FILES, self.DIR_NOBODY, self.DIR_SMALLTHUMBS, char_id, '.', self.SAVE_IMG_EXT])
		###
		return url

class PuzzleId2Name(Id2Name):

	def __init__(self):
		from collage.puzzle.settings import MEDIA_URL, SAVE_IMG_EXT, MEDIA_URL_FILES, DIR_NOBODY, DIR_AUTH, DIR_SMALLTHUMBS
		from collage.puzzle.models import STRETCH_CHOISES, TYPE_CHOISES, SIZE_CHOISES, EFFECT_CHOISES
		###
		self.STRETCH_CHOISES = STRETCH_CHOISES
		self.TYPE_CHOISES = TYPE_CHOISES
		self.SIZE_CHOISES = SIZE_CHOISES
		self.EFFECT_CHOISES = EFFECT_CHOISES
		###
		self.SAVE_IMG_EXT = SAVE_IMG_EXT
		self.MEDIA_URL = MEDIA_URL
		self.MEDIA_URL_FILES = MEDIA_URL_FILES
		self.DIR_NOBODY = DIR_NOBODY
		self.DIR_AUTH = DIR_AUTH
		self.DIR_SMALLTHUMBS = DIR_SMALLTHUMBS

	def set(self, row, auth=False):
		row['price'] = PuzzlePrice.objects.get(size_id=row['img_size']).price
		row['summ'] = float(row['price']) * float(row['qty'])
		###
		row['image'] = self.image(row['pth'], row['char_id'], auth)
		###
		row['img_stretch'] = self.i2n(int(row['img_stretch']), self.STRETCH_CHOISES)
		row['img_type'] = self.i2n(int(row['img_type']), self.TYPE_CHOISES)
		row['img_size'] = self.i2n(int(row['img_size']), self.SIZE_CHOISES)
		row['img_effect'] = self.i2n(int(row['img_effect']), self.EFFECT_CHOISES)
		###
		return row

	def image(self, pth=None, char_id='', auth=False):
		url = ''
		###
		if auth:
			url = ''.join([pth, self.DIR_SMALLTHUMBS, char_id, '.', self.SAVE_IMG_EXT])
		else:
			url = ''.join([self.MEDIA_URL, self.MEDIA_URL_FILES, self.DIR_NOBODY, self.DIR_SMALLTHUMBS, char_id, '.', self.SAVE_IMG_EXT])
		###
		return url

class MosaicId2Name(Id2Name):

	def __init__(self):
		from collage.mosaic.settings import MEDIA_URL, SAVE_IMG_EXT, MEDIA_URL_FILES, DIR_NOBODY, DIR_AUTH, DIR_SMALLTHUMBS
		from collage.mosaic.models import EFFECT_CHOISES, SIZE_CHOISES_ADMIN
		###
		self.SAVE_IMG_EXT = SAVE_IMG_EXT
		self.MEDIA_URL = MEDIA_URL
		self.MEDIA_URL_FILES = MEDIA_URL_FILES
		self.DIR_NOBODY = DIR_NOBODY
		self.DIR_AUTH = DIR_AUTH
		self.DIR_SMALLTHUMBS = DIR_SMALLTHUMBS
		###
		self.EFFECT_CHOISES = EFFECT_CHOISES
		self.SIZE_CHOISES_ADMIN = SIZE_CHOISES_ADMIN

	def set(self, row, auth=False):
		row['price'] = MosaicPrice.objects.get(size_id=row['table_size']).price
		row['summ'] = float(row['price']) * float(row['qty'])
		###
		row['image'] = self.image(row, auth)
		###
		row['table_size'] = self.i2n(int(row['table_size']), self.SIZE_CHOISES_ADMIN)
		row['effect'] = self.i2n(int(row['effect']), self.EFFECT_CHOISES)
		###
		return row

	def image(self, row={}, auth=False):
		url = ''
		###
		char_id = ''
		###
		for i in xrange(9):
			if not row['f_%s' % (i,)] == '':
				char_id = row['f_%s' % (i,)]
				###
				break
		###
		if auth:
			url = ''.join([row['pth'], self.DIR_SMALLTHUMBS, char_id, '.', self.SAVE_IMG_EXT])
		else:
			url = ''.join([self.MEDIA_URL, self.MEDIA_URL_FILES, self.DIR_NOBODY, self.DIR_SMALLTHUMBS, char_id, '.', self.SAVE_IMG_EXT])
		###
		return url

class CropData(CropId2Name):

	def __init__(self, request):
		super(CropData, self).__init__()
		###
		self.request = request
		self.user = request.user
		self.data = request.CART.get_data(self.user.is_authenticated(), 1)
		self.total = 0.00
		self.f = OptionForm()

	def auth(self):
		option = []
		###
		co = OptionFiles.objects.filter(file__in=Files.objects.filter(user=self.user, char_id__in=[v['opt_id'] for v in self.data]))
		###
		for i in co:
			row = self.f.getDataRow(i)
			###
			row['char_id'] = i.file.char_id
			row['pth'] = i.file.pth
			row['frame_id'] = i.frame.id
			row['packaging_id'] = i.packaging.id
			###
			row = self.set(row, True)
			###
			self.total = self.total + float(row['summ'])
			###
			option.append(row)
		###
		return option

	def nobody(self):
		option = []
		###
		clo = CookieListOptions()
		opts = clo.get_data(self.request)
		###
		for j in self.data:
			for i in opts:
				if i['char_id'] == j['opt_id']:
					i['frame_id'] = i['frame']
					i['packaging_id'] = i['packaging']
					###
					i['pth'] = None
					i['frame'] = Frames.objects.get(pk=i['frame_id'])
					i['packaging'] = Packaging.objects.get(pk=i['packaging_id'])
					###
					i = self.set(i, False)
					###
					self.total = self.total + float(i['summ'])
					###
					option.append(i)
					###
					break
		###
		return option

class PuzzleData(PuzzleId2Name):

	def __init__(self, request):
		super(PuzzleData, self).__init__()
		###
		self.request = request
		self.user = request.user
		self.data = request.CART.get_data(self.user.is_authenticated(), 2)
		self.total = 0.00
		self.f = PuzzleForm()

	def auth(self):
		option = []
		###
		po = PuzzleOption.objects.filter(file__in=PuzzleFiles.objects.filter(user=self.user, char_id__in=[v['opt_id'] for v in self.data]))
		###
		for i in po:
			row = self.f.getDataRow(i)
			###
			row['char_id'] = i.file.char_id
			row['pth'] = i.file.pth
			row['frame_id'] = i.frame.id
			row['packaging_id'] = i.packaging.id
			###
			row = self.set(row, True)
			###
			self.total = self.total + float(row['summ'])
			###
			option.append(row)
		###
		return option

	def nobody(self):
		option = []
		###
		cpo = CookiePuzzleOption()
		opts = cpo.get_data(self.request)
		###
		for j in self.data:
			for i in opts:
				if i['char_id'] == j['opt_id']:
					i['frame_id'] = i['frame']
					i['packaging_id'] = i['packaging']
					###
					i['pth'] = None
					i['frame'] = Frames.objects.get(pk=i['frame_id'])
					i['packaging'] = Packaging.objects.get(pk=i['packaging_id'])
					###
					i = self.set(i, False)
					###
					self.total = self.total + float(i['summ'])
					###
					option.append(i)
					###
					break
		###
		return option

class MosaicData(MosaicId2Name):

	def __init__(self, request):
		super(MosaicData, self).__init__()
		###
		self.request = request
		self.user = request.user
		self.data = request.CART.get_data(self.user.is_authenticated(), 3)
		self.total = 0.00
		self.f = MosaicOptionForm()

	def auth(self):
		option = []
		###
		mo = MosaicOption.objects.filter(opt_id__in=[v['opt_id'] for v in self.data])
		###
		for i in mo:
			row = self.f.getDataRow(i)
			###
			row['frame_id'] = i.frame.id
			row['packaging_id'] = i.packaging.id
			###
			row = self.set(row, True)
			###
			self.total = self.total + float(row['summ'])
			###
			option.append(row)
		###
		return option

	def nobody(self):
		option = []
		###
		cmo = CookieMosaicOption()
		opts = cmo.get_data(self.request)
		###
		for j in self.data:
			for i in opts:
				if i['opt_id'] == j['opt_id']:
					i['frame_id'] = i['frame']
					i['packaging_id'] = i['packaging']
					###
					i['frame'] = Frames.objects.get(pk=i['frame_id'])
					i['packaging'] = Packaging.objects.get(pk=i['packaging_id'])
					###
					i = self.set(i, False)
					###
					self.total = self.total + float(i['summ'])
					###
					option.append(i)
					###
					break
		###
		return option

def show(request):
	cd = CropData(request)
	crop_option = cd.get()
	###
	pd = PuzzleData(request)
	puzzle_option = pd.get()
	###
	md = MosaicData(request)
	mosaic_option = md.get()
	###
	total = cd.total + pd.total + md.total
	###
	data = {
		'crop_option':crop_option,
		'puzzle_option':puzzle_option,
		'mosaic_option':mosaic_option,
		'crop_total':cd.total,
		'puzzle_total':pd.total,
		'mosaic_total':md.total,
		'total':total,
	}
	###
	return render(request, 'cart_show.html', data)

def delete(request):
	auth = request.user.is_authenticated()	
	###
	if request.CART.delete(request.GET.get('opt_id', None), int(request.GET.get('type_id', None)), auth):
		messages.success(request, 'Изображение удалено из корзины')
	else:
		messages.error(request, 'Изображение не найдено')
	###
	return HttpResponseRedirect(reverse('cart.views.show'))
