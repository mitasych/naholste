# -*- coding: utf-8 -*-

import os
import shutil

from collage.cart.settings import *
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, HttpResponseBadRequest
from django.shortcuts import render
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage

from collage.common.helpers import CookieListOptions, CookiePuzzleOption, CookieMosaicOption
from collage.crop.models import CropPrice, Files, OptionFiles, Frames, Packaging
from collage.crop.forms import OptionForm
from collage.puzzle.models import PuzzlePrice, PuzzleFiles, PuzzleOption
from collage.puzzle.forms import OptionForm as PuzzleForm
from collage.mosaic.models import MosaicPrice, MosaicOption
from collage.mosaic.forms import MosaicOptionForm
from collage.cart.models import Order, OrderOption
from collage.cart.forms import OrderForm, AuthCartForm

from collage.crop.views import ReloadCrop, DataImg
from collage.puzzle.views import ReloadPuzzle

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
		from collage.mosaic.models import EFFECT_CHOISES, SIZE_CHOISES_ADMIN, TYPE_CHOISES
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
		self.TYPE_CHOISES = TYPE_CHOISES

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
			row['table_type'] = self.i2n(int(row['table_type']), self.TYPE_CHOISES)
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
					i['table_type'] = self.i2n(int(i['table_type']), self.TYPE_CHOISES)
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

class Opt2Text(object):

	def crop_list(self, o={}):
		return [
			''.join([u'Натяжка', ' - ',  o['img_stretch'],]),
			''.join([u'Ориентация', ' - ', o['img_type'],]),
			''.join([u'Размер', ' - ',  o['img_size'],]),
			''.join([u'Эффекты', ' - ',  o['img_effect'],]),
			''.join([u'Рамка', ' - ',  o['frame'].__unicode__(),]),
			''.join([u'Упаковка', ' - ',  o['packaging'].__unicode__(),]),
			''.join([u'Количество', ' - ',  str(o['qty']),]),
			''.join([u'Цена', ' - ',  str(o['price']),]),
			''.join([u'Сумма', ' - ',  str(o['summ']),]),
			''.join([u'Верхняя координата X', ' - ',  str(o['x1']),]),
			''.join([u'Верхняя координата Y', ' - ',  str(o['y1']),]),
			''.join([u'Нижняя координата X', ' - ',  str(o['x2']),]),
			''.join([u'Нижняя координата Y', ' - ',  str(o['y2']),]),
		]

	def crop(self, o={}):
		return '\n'.join(self.crop_list(o))

	def puzzle_list(self, o={}):
		return [
			''.join([u'Натяжка', ' - ',  o['img_stretch'],]),
			''.join([u'Ориентация', ' - ', o['img_type'],]),
			''.join([u'Размер', ' - ',  o['img_size'],]),
			''.join([u'Эффекты', ' - ',  o['img_effect'],]),
			''.join([u'Рамка', ' - ',  o['frame'].__unicode__(),]),
			''.join([u'Упаковка', ' - ',  o['packaging'].__unicode__(),]),
			''.join([u'Количество', ' - ',  str(o['qty']),]),
			''.join([u'Цена', ' - ',  str(o['price']),]),
			''.join([u'Сумма', ' - ',  str(o['summ']),]),
		]

	def puzzle(self, o={}):
		return '\n'.join(self.puzzle_list(o))

	def mosaic_list(self, o={}):
		return [
			''.join([u'Тип', ' - ',  o['table_type'],]),
			''.join([u'Размер', ' - ',  o['table_size'],]),
			''.join([u'Эффекты', ' - ',  o['effect'],]),
			''.join([u'Рамка', ' - ',  o['frame'].__unicode__(),]),
			''.join([u'Упаковка', ' - ',  o['packaging'].__unicode__(),]),
			''.join([u'Количество', ' - ',  str(o['qty']),]),
			''.join([u'Цена', ' - ',  str(o['price']),]),
			''.join([u'Сумма', ' - ',  str(o['summ']),]),
		]

	def mosaic(self, o={}):
		return '\n'.join(self.mosaic_list(o))

class OrderFiles(object):

	auth = False
	zipf = ''

	def __init__(self, order_id=0, data={}, user=None):
		self.auth = (user.is_authenticated() and user.is_active) and True or False
		###
		order_pth = '/'.join([ORDERS_DIR, str(order_id)])
		order_holst = '/'.join([order_pth, 'holst'])
		order_multy = '/'.join([order_pth, 'multy'])
		order_collage = '/'.join([order_pth, 'collage'])
		###
		if not os.path.isdir(order_pth):
			os.makedirs(order_pth)
			os.makedirs(order_holst)
			os.makedirs(order_multy)
			os.makedirs(order_collage)
		### Обрабатываем на холсте
		for o in data['crop_option']:
			self.crop(o, order_holst)
		### Обрабатываем мультихолст
		for o in data['puzzle_option']:
			self.puzzle(o, order_multy)
		### Обрабатываем коллаж
		for o in data['mosaic_option']:
			self.mosaic(o, order_collage)
		### Пакуем в ZIP
		self.to_zip(str(order_id), order_pth)
		### Удалим мусор
		shutil.rmtree(order_pth)

	def zipname(self):
		return self.zipf

	def to_zip(self, order_id='', order_pth=''):
		from contextlib import closing
		from zipfile import ZipFile, ZIP_DEFLATED
		###
		zipf = '/'.join([ORDERS_DIR, '%s.zip' % (order_id,)])
		self.zipf = ''.join([MEDIA_URL, MEDIA_URL_ORDERS, '%s.zip' % (order_id,)])
		###
		with closing(ZipFile(zipf, "w", ZIP_DEFLATED)) as z:
			for root, dirs, files in os.walk(order_pth):
				for fn in files:
					absfn = os.path.join(root, fn)
					###
					zfn = absfn[len(order_pth)+len(os.sep):]
					###
					z.write(absfn, zfn)

	def mosaic(self, o={}, order_collage=''):
		from collage.mosaic.settings import SAVE_IMG_EXT, DIR_NOBODY, PATH_PJT, FILES_DIR
		###
		dist_pth = '/'.join([order_collage, str(o['opt_id'])])
		###
		os.makedirs(dist_pth)
		###
		dist_txt = '/'.join([dist_pth, 'info.txt',])
		###
		with open(dist_txt, 'w') as f:
			f.write("\n".join([v for v in o['options']]).encode('utf-8'))
			###
			f.close()
		###
		for i in xrange(9):
			k = 'f_%s' % (i,)
			###
			if not o[k] == '':
				dist = '/'.join([dist_pth, '%s_%s.%s' % (i, o[k], SAVE_IMG_EXT),])
				###
				if self.auth:
					src = ''.join([PATH_PJT, o['pth'], o[k], '.', SAVE_IMG_EXT])
				else:
					src = ''.join([FILES_DIR, DIR_NOBODY, o[k], '.', SAVE_IMG_EXT])
				###
				if os.path.isfile(src):
					shutil.copyfile(src, dist)

	def puzzle(self, o={}, order_multy=''):
		from collage.puzzle.settings import SAVE_IMG_EXT, DIR_NOBODY, PATH_PJT, FILES_DIR
		###
		dist_pth = '/'.join([order_multy, o['char_id'],])
		###
		os.makedirs(dist_pth)
		###
		dist = '/'.join([dist_pth, '%s.%s' % (o['char_id'], SAVE_IMG_EXT),])
		dist_txt = '/'.join([dist_pth, 'info.txt',])
		###
		if self.auth:
			src = ''.join([PATH_PJT, o['pth'], o['char_id'], '.', SAVE_IMG_EXT])
		else:
			src = ''.join([FILES_DIR, DIR_NOBODY, o['char_id'], '.', SAVE_IMG_EXT])
		###
		if os.path.isfile(src):
			shutil.copyfile(src, dist)
			###
			with open(dist_txt, 'w') as f:
				f.write("\n".join([v for v in o['options']]).encode('utf-8'))
				###
				f.close()

	def crop(self, o={}, order_holst=''):
		from collage.crop.settings import SAVE_IMG_EXT, DIR_NOBODY, PATH_PJT, FILES_DIR
		###
		dist_pth = '/'.join([order_holst, o['char_id'],])
		###
		os.makedirs(dist_pth)
		###
		dist = '/'.join([dist_pth, '%s.%s' % (o['char_id'], SAVE_IMG_EXT),])
		dist_txt = '/'.join([dist_pth, 'info.txt',])
		###
		if self.auth:
			src = ''.join([PATH_PJT, o['pth'], o['char_id'], '.', SAVE_IMG_EXT])
		else:
			src = ''.join([FILES_DIR, DIR_NOBODY, o['char_id'], '.', SAVE_IMG_EXT])
		###
		if os.path.isfile(src):
			shutil.copyfile(src, dist)
			###
			with open(dist_txt, 'w') as f:
				f.write("\n".join([v for v in o['options']]).encode('utf-8'))
				###
				f.close()

def log_in(request):
	user = request.user
	###
	if (user.is_authenticated() == False):
		if request.method == 'POST':
			form = AuthCartForm(request.POST)
			###
			if form.is_valid():
				send_data = form.cleaned_data
				###
				user = authenticate(username=send_data['user'], password=send_data['password'])
				###
				if user is not None:
					if user.is_active:
						login(request, user)
						###
						if send_data['reload']:
							rc = ReloadCrop(request)
							rc.reload()
							###
							rp = ReloadPuzzle(request)
							rp.reload()
							###
							request.CART.reload(True)
							###
							response = HttpResponseRedirect(reverse('cart.views.delivery'))
							###
							response = rc.clear(response)
							return rp.clear(response)
						else:
							HttpResponseRedirect(reverse('cart.views.delivery'))
					else:
						messages.error(request, 'Ваш профиль заблокирован')
				else:
					messages.error(request, 'Не првильно указан логин или пароль')
		else:
			form = AuthCartForm()
		###
		data = {
			'form':form,
		}
	else:
		return HttpResponseRedirect(reverse('cart.views.delivery'))
	###
	return render(request, 'cart_login.html', data)

def show(request):
	user = request.user
	###
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
		'to_url':(user.is_authenticated() and user.is_active) and '/cart/delivery/' or '/cart/login/',
	}
	###
	return render(request, 'cart_show.html', data)

def order(request):
	di = DataImg()
	o2t = Opt2Text()
	###
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
	if (len(crop_option) == 0) and (len(puzzle_option) == 0) and (len(mosaic_option) == 0):
		messages.error(request, 'Ваша корзина пуста')
		###
		return HttpResponseRedirect(reverse('cart.views.show'))
	###
	user = request.user
	###
	is_create = False
	###
	if request.method == 'POST':
		is_create = True
		###
		form = OrderForm(request.POST)
		###
		if form.is_valid():
			send_data = form.cleaned_data
			###
			order = Order.objects.create(
				price=total,
				address=send_data['address'],
				email=send_data['email'],
				name=send_data['name'],
				phone=send_data['phone'],
			)
			###
			if (user.is_authenticated() and user.is_active):
				order.user = user
			###
			order.save()
			### Crop
			for o in crop_option:
				order_opt = OrderOption.objects.create(
					order_id=order.id,
					type_id=1,
					char_id=o['char_id'],
					frame=o['frame'],
					packaging=o['packaging']
				)
				###
				for i in xrange(9):
					order_opt.__setattr__('f_%s' % (i,), '')
				### Перещитаем координаты из тумбы в оригинал
				if (user.is_authenticated() and user.is_active):
					size = di.coord_auth(o['char_id'], o['pth'], {'x1':o['x1'], 'y1':o['y1'], 'x2':o['x2'], 'y2':o['y2']})
				else:
					size = di.coord_nobody(o['char_id'], {'x1':o['x1'], 'y1':o['y1'], 'x2':o['x2'], 'y2':o['y2']})
				###
				o['x1'] = size['x1']
				o['y1'] = size['y1']
				o['x2'] = size['x2']
				o['y2'] = size['y2']
				###
				order_opt.options = o2t.crop(o)
				o['options'] = o2t.crop_list(o)
				###
				order_opt.save()
			### Puzzle
			for o in puzzle_option:
				order_opt = OrderOption.objects.create(
					order_id=order.id,
					type_id=2,
					char_id=o['char_id'],
					frame=o['frame'],
					packaging=o['packaging']
				)
				###
				for i in xrange(9):
					order_opt.__setattr__('f_%s' % (i,), '')
				###
				order_opt.options = o2t.puzzle(o)
				o['options'] = o2t.puzzle_list(o)
				###
				order_opt.save()
			### Mosaic
			for o in mosaic_option:
				order_opt = OrderOption.objects.create(
					order_id=order.id,
					type_id=3,
					char_id='',
					frame=o['frame'],
					packaging=o['packaging']
				)
				###
				for i in xrange(9):
					f = 'f_%s' % (i,)
					###
					order_opt.__setattr__(f, o[f])
				###
				order_opt.options = o2t.mosaic(o)
				o['options'] = o2t.mosaic_list(o)
				###
				order_opt.save()
			### Очистим корзину
			#request.CART.clear()
			###
			messages.success(request, u'Ваш заказ №%s принят.' % (order.id,))
			### Отправим подтверждение на мыло администратору
			data = {
				'order_id':order.id,
				'crop_option':crop_option,
				'puzzle_option':puzzle_option,
				'mosaic_option':mosaic_option,
			}
			###
			t = loader.get_template('cart_order_mail.html')
			c = RequestContext(request, data)
			###
			html = t.render(c)
			### Формируем письмо клиенту
			html_user = html.replace(u':TITLE', u'Ваш заказ №').replace(u':ZIP_URL', '')
			###
			msg = EmailMessage(u'Ваш заказ №%s' % (order.id,), html_user, EMAIL_FROM, [send_data['email']])
			msg.content_subtype = "html"
			msg.send()
			### Формируем данные для админа
			of = OrderFiles(order.id, data, user)
			###
			a_zip = u'''
			<a href="%s">Архив с данными</a><br /><br />
			''' % (of.zipname(),)
			###
			html_admin = html.replace(u':TITLE', u'Поступил заказ №').replace(u':ZIP_URL', a_zip)
			###
			msg = EmailMessage(u'Новый заказ №%s' % (order.id,), html_user, EMAIL_FROM, EMAILS_LIST)
			msg.content_subtype = "html"
			msg.send()
			###
			return HttpResponseRedirect(reverse('common.views.index'))
	###
	if not is_create:
		if (user.is_authenticated() and user.is_active):
			def_data = {
				'email':user.email,
			}
			###
			form = OrderForm(initial=def_data)
		else:
			form = OrderForm()
	###
	for o in crop_option:
		o['options'] = o2t.crop_list(o)
	for o in puzzle_option:
		o['options'] = o2t.puzzle_list(o)
	for o in mosaic_option:
		o['options'] = o2t.mosaic_list(o)
	###
	data = {
		'form':form,
		'crop_option':crop_option,
		'puzzle_option':puzzle_option,
		'mosaic_option':mosaic_option,
	}
	###
	return render(request, 'cart_order.html', data)
	
def delete(request):
	auth = request.user.is_authenticated()	
	###
	if request.CART.delete(request.GET.get('opt_id', None), int(request.GET.get('type_id', None)), auth):
		messages.success(request, 'Изображение удалено из корзины')
	else:
		messages.error(request, 'Изображение не найдено')
	###
	return HttpResponseRedirect(reverse('cart.views.show'))

def delivery(request):
	return render(request, 'cart_delivery.html', {})
