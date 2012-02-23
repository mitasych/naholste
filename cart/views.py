# -*- coding: utf-8 -*-

import os
import shutil
import threading

from collage.cart.settings import *
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage

from collage.account.models import UserProfile
from collage.common.decorators import reload, reload_data
from collage.crop.models import CropSize, Crop
from collage.puzzle.models import PuzzleSize, Puzzle
from collage.mosaic.models import MosaicSize, Mosaic
from collage.cart.models import Order, OrderOption
from collage.cart.forms import OrderForm, AuthCartForm

from collage.crop.views import DataImg as Dic
from collage.puzzle.views import DataImg as Dip

class Id2Name(object):

	request = None
	user = None
	data = []
	total = 0.00

	def __init__(self, request, settings, models, t):
		if hasattr(models, 'TYPE_CHOISES'):
			self.TYPE_CHOISES = models.TYPE_CHOISES
		###
		self.EFFECT_CHOISES = models.EFFECT_CHOISES
		###
		self.IMG_EXT = settings.IMG_EXT
		self.MEDIA_URL = settings.MEDIA_URL
		self.MEDIA_URL_FILES = settings.MEDIA_URL_FILES
		self.DIR_SMALLTHUMBS = settings.DIR_SMALLTHUMBS
		###
		self.request = request
		self.user = request.user
		self.auth = (self.user.is_authenticated() and self.user.is_active) and True or False
		self.data = request.CART.get_data(self.auth, t)
		self.total = 0.00

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

	def image(self, opt):
		if hasattr(opt, 'img'):
			return ''.join([self.MEDIA_URL, self.MEDIA_URL_FILES, self.DIR_SMALLTHUMBS, opt.img, '.', self.IMG_EXT])
		###
		if hasattr(opt, 'f_0'):
			if opt.table_type == 1:
				len_size = 9
			if opt.table_type == 2:
				len_size = 7
			if opt.table_type == 3:
				len_size = 7
			###
			img = 'no'
			###
			for i in xrange(len_size):
				k = 'f_%s' % i
				v = getattr(opt, k)
				###
				if not v == '':
					img = v
					###
					break
			###
			return ''.join([self.MEDIA_URL, self.MEDIA_URL_FILES, self.DIR_SMALLTHUMBS, img, '.', self.IMG_EXT])

	def get(self, opt, di=None):
		row = {'id':opt.id,}
		###
		if opt.frame is None:
			price_frame = 0.00
		else:
			price_frame = float(opt.frame.price)
		###
		if opt.packaging is None:
			price_packaging = 0.00
		else:
			price_packaging = float(opt.packaging.price)
		###
		row['price'] = float(opt.img_size.price) + price_frame + price_packaging
		row['summ'] = row['price'] * float(opt.qty)
		###
		row['image'] = self.image(opt)
		###
		if hasattr(opt, 'img'):
			row['img'] = opt.img
		###
		if hasattr(opt, 'f_0'):
			for i in xrange(9):
				k = 'f_%s' % i
				row[k] = getattr(opt, k)
		###
		if hasattr(opt, 'table_type'):
			row['table_type'] = self.i2n(int(opt.table_type), self.TYPE_CHOISES)
		###
		if hasattr(opt, 'img_stretch'):
			row['img_stretch'] = opt.img_stretch.__unicode__()
		###
		if hasattr(opt, 'img_type'):
			row['img_type'] = self.i2n(int(opt.img_type), self.TYPE_CHOISES)
		###
		row['img_size'] = opt.img_size.__unicode__()
		###
		row['img_effect'] = self.i2n(int(opt.img_effect), self.EFFECT_CHOISES)
		###
		if opt.frame is None:
			row['frame'] = u'Нет'
		else:
			row['frame'] = opt.frame.__unicode__()
		###
		if opt.packaging is None:
			row['packaging'] = u'Нет'
		else:
			row['packaging'] = opt.packaging.__unicode__()
		###
		row['qty'] = int(opt.qty)
		###
		if hasattr(opt, 'x1'):
			size = di.coord(opt.img, {'x1':int(opt.x1), 'y1':int(opt.y1), 'x2':int(opt.x2), 'y2':int(opt.y2)})
			row['x1'] = size['x1']
			row['y1'] = size['y1']
			row['x2'] = size['x2']
			row['y2'] = size['y2']
		###
		return row

class CropData(Id2Name):

	def __init__(self, request):
		from collage.crop import models
		from collage.crop import settings
		###
		super(CropData, self).__init__(request, settings, models, 1)

	def get(self):
		option = []
		###
		p = Crop.objects.filter(pk__in=[v['id'] for v in self.data])
		###
		dic = Dic()
		###
		for opt in p:
			row = super(CropData, self).get(opt, di=dic)
			self.total = self.total + float(row['summ'])
			option.append(row)
		###
		return option

class PuzzleData(Id2Name):

	def __init__(self, request):
		from collage.puzzle import models
		from collage.puzzle import settings
		###
		super(PuzzleData, self).__init__(request, settings, models, 2)

	def get(self):
		option = []
		###
		p = Puzzle.objects.filter(pk__in=[v['id'] for v in self.data])
		###
		dip = Dip()
		###
		for opt in p:
			row = super(PuzzleData, self).get(opt, di=dip)
			self.total = self.total + float(row['summ'])
			option.append(row)
		###
		return option

class MosaicData(Id2Name):

	def __init__(self, request):
		from collage.mosaic import models
		from collage.mosaic import settings
		###
		super(MosaicData, self).__init__(request, settings, models, 3)

	def get(self):
		option = []
		###
		p = Mosaic.objects.filter(pk__in=[v['id'] for v in self.data])
		###
		for opt in p:
			row = super(MosaicData, self).get(opt)
			self.total = self.total + float(row['summ'])
			option.append(row)
		###
		return option

class Opt2Text(object):

	def crop_list(self, o={}):
		return [
			''.join([u'Натяжка', ' - ',  o['img_stretch'],]),
			''.join([u'Ориентация', ' - ', o['img_type'],]),
			''.join([u'Размер', ' - ',  o['img_size'],]),
			''.join([u'Эффекты', ' - ',  o['img_effect'],]),
			''.join([u'Рамка', ' - ',  o['frame'],]),
			''.join([u'Упаковка', ' - ',  o['packaging'],]),
			''.join([u'Верхняя координата X', ' - ',  str(o['x1']),]),
			''.join([u'Верхняя координата Y', ' - ',  str(o['y1']),]),
			''.join([u'Нижняя координата X', ' - ',  str(o['x2']),]),
			''.join([u'Нижняя координата Y', ' - ',  str(o['y2']),]),
			''.join([u'Количество', ' - ',  str(o['qty']),]),
			''.join([u'Цена', ' - ',  str(o['price']),]),
			''.join([u'Сумма', ' - ',  str(o['summ']),]),
		]

	def crop(self, o={}):
		return '\n'.join(self.crop_list(o))

	def puzzle_list(self, o={}):
		return [
			''.join([u'Натяжка', ' - ',  o['img_stretch'],]),
			''.join([u'Размер', ' - ',  o['img_size'],]),
			''.join([u'Эффекты', ' - ',  o['img_effect'],]),
			''.join([u'Рамка', ' - ',  o['frame'],]),
			''.join([u'Упаковка', ' - ',  o['packaging'],]),
			''.join([u'Верхняя координата X', ' - ',  str(o['x1']),]),
			''.join([u'Верхняя координата Y', ' - ',  str(o['y1']),]),
			''.join([u'Нижняя координата X', ' - ',  str(o['x2']),]),
			''.join([u'Нижняя координата Y', ' - ',  str(o['y2']),]),
			''.join([u'Количество', ' - ',  str(o['qty']),]),
			''.join([u'Цена', ' - ',  str(o['price']),]),
			''.join([u'Сумма', ' - ',  str(o['summ']),]),
		]

	def puzzle(self, o={}):
		return '\n'.join(self.puzzle_list(o))

	def mosaic_list(self, o={}):
		return [
			''.join([u'Тип', ' - ',  o['table_type'],]),
			''.join([u'Размер', ' - ',  o['img_size'],]),
			''.join([u'Эффекты', ' - ',  o['img_effect'],]),
			''.join([u'Рамка', ' - ',  o['frame'],]),
			''.join([u'Упаковка', ' - ',  o['packaging'],]),
			''.join([u'Количество', ' - ',  str(o['qty']),]),
			''.join([u'Цена', ' - ',  str(o['price']),]),
			''.join([u'Сумма', ' - ',  str(o['summ']),]),
		]

	def mosaic(self, o={}):
		return '\n'.join(self.mosaic_list(o))

class OrderFiles(object):

	auth = False
	zipf = ''

	def __init__(self, order_id=0, data={}, auth=False):
		self.auth
		###
		order_pth = '/'.join([ORDERS_DIR, str(order_id)])
		order_crop = '/'.join([order_pth, 'crop'])
		order_puzzle = '/'.join([order_pth, 'puzzle'])
		order_mosaic = '/'.join([order_pth, 'mosaic'])
		###
		if not os.path.isdir(order_pth):
			os.makedirs(order_pth)
			os.makedirs(order_crop)
			os.makedirs(order_puzzle)
			os.makedirs(order_mosaic)
		### Обрабатываем на холсте
		for o in data['crop_option']:
			self.crop(o, order_crop)
		### Обрабатываем мультихолст
		for o in data['puzzle_option']:
			self.puzzle(o, order_puzzle)
		### Обрабатываем коллаж
		for o in data['mosaic_option']:
			self.mosaic(o, order_mosaic)
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

	def mosaic(self, o={}, order_mosaic=''):
		from collage.mosaic.settings import IMG_EXT, PATH_PJT, FILES_DIR
		###
		opt_id = str(o['id'])
		###
		dist_pth = '/'.join([order_mosaic, opt_id])
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
				dist = '/'.join([dist_pth, '%s_%s.%s' % (i, o[k], IMG_EXT),])
				###
				src = ''.join([FILES_DIR, o[k], '.', IMG_EXT])
				###
				if os.path.isfile(src):
					shutil.copyfile(src, dist)

	def puzzle(self, o={}, order_puzzle=''):
		from collage.puzzle.settings import IMG_EXT, PATH_PJT, FILES_DIR
		###
		opt_id = str(o['id'])
		###
		dist_pth = '/'.join([order_puzzle, opt_id,])
		###
		os.makedirs(dist_pth)
		###
		dist = '/'.join([dist_pth, '%s.%s' % (o['img'], IMG_EXT),])
		dist_txt = '/'.join([dist_pth, 'info.txt',])
		###
		src = ''.join([FILES_DIR, o['img'], '.', IMG_EXT])
		###
		if os.path.isfile(src):
			shutil.copyfile(src, dist)
			###
			with open(dist_txt, 'w') as f:
				f.write("\n".join([v for v in o['options']]).encode('utf-8'))
				###
				f.close()

	def crop(self, o={}, order_crop=''):
		from collage.crop.settings import IMG_EXT, PATH_PJT, FILES_DIR
		###
		opt_id = str(o['id'])
		###
		dist_pth = '/'.join([order_crop, opt_id,])
		###
		os.makedirs(dist_pth)
		###
		dist = '/'.join([dist_pth, '%s.%s' % (o['img'], IMG_EXT),])
		dist_txt = '/'.join([dist_pth, 'info.txt',])
		###
		src = ''.join([FILES_DIR, o['img'], '.', IMG_EXT])
		###
		if os.path.isfile(src):
			shutil.copyfile(src, dist)
			###
			with open(dist_txt, 'w') as f:
				f.write("\n".join([v for v in o['options']]).encode('utf-8'))
				###
				f.close()

class HiddenWork(threading.Thread):

	def setData(self, request, data, email, auth):
		self.request = request
		self.data = data
		self.email = email
		self.auth = auth

	def run(self):
		t = loader.get_template('cart_order_mail.html')
		c = RequestContext(self.request, self.data)
		###
		html = t.render(c)
		### Формируем письмо клиенту
		html_user = html.replace(u':TITLE', u'Ваш заказ №').replace(u':ZIP_URL', '')
		###
		msg = EmailMessage(u'Ваш заказ №%s' % self.data['order_id'], html_user, EMAIL_FROM, [self.email])
		msg.content_subtype = "html"
		msg.send()
		### Формируем данные для админа
		of = OrderFiles(self.data['order_id'], self.data, self.auth)
		###
		a_zip = u'''
		<a href="%s">Архив с данными</a><br /><br />
		''' % (of.zipname(),)
		###
		html_admin = html.replace(u':TITLE', u'Поступил заказ №').replace(u':ZIP_URL', a_zip)
		###
		msg = EmailMessage(u'Новый заказ №%s' % self.data['order_id'], html_user, EMAIL_FROM, EMAILS_LIST)
		msg.content_subtype = "html"
		msg.send()

HW = HiddenWork()

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
		'to_url':cd.auth and '/cart/shiping/' or '/cart/login/',
	}
	###
	return render(request, 'cart_show.html', data)

def delete(request):
	auth = request.user.is_authenticated()	
	###
	if request.CART.delete(request.GET.get('id', None), int(request.GET.get('t', None)), auth):
		messages.success(request, 'Изображение удалено из корзины')
	else:
		messages.error(request, 'Изображение не найдено')
	###
	return HttpResponseRedirect(reverse('cart.views.show'))

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
				user = authenticate(username=send_data['email'], password=send_data['password'])
				###
				if user is not None:
					if user.is_active:
						login(request, user)
						###
						nouser = request.NOUSER.get()
						###
						reload_data(Crop, user, nouser)
						reload_data(Puzzle, user, nouser)
						reload_data(Mosaic, user, nouser)
						###
						request.CART.reload(True)
						###
						return HttpResponseRedirect(reverse('cart.views.shiping'))
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
		return HttpResponseRedirect(reverse('cart.views.shiping'))
	###
	return render(request, 'cart_login.html', data)

def shiping(request):
	return render(request, 'cart_shiping.html', {})

def order(request):
	dic = Dic()
	dip = Dip()
	o2t = Opt2Text()
	user = request.user
	auth = (user.is_authenticated() and user.is_active) and True or False
	is_create = False
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
				shiping_price=0,
				address=send_data['address'],
				email=send_data['email'],
				name=send_data['name'],
				phone=send_data['phone'],
			)
			###
			if auth:
				order.user = user
			else:
				order.nouser = request.NOUSER.get()
			###
			order.save()
			### Crop
			for o in crop_option:
				order_opt = OrderOption.objects.create(
					order=order,
					type_id=1,
					price=o['summ'],
					img=o['img']
				)
				###
				for i in xrange(9):
					order_opt.__setattr__('f_%s' % (i,), '')
				###
				order_opt.options = o2t.crop(o)
				o['options'] = o2t.crop_list(o)
				###
				order_opt.save()
			### Puzzle
			for o in puzzle_option:
				order_opt = OrderOption.objects.create(
					order=order,
					type_id=2,
					price=o['summ'],
					img=o['img']
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
					order=order,
					type_id=3,
					price=o['summ'],
					img=''
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
			request.CART.clear()
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
			HW.setData(request, data, send_data['email'], auth)
			HW.start()
			###
			return HttpResponseRedirect(reverse('common.views.index'))
	###
	if not is_create:
		if auth:
			prof = UserProfile.objects.get(user=user.id)
			###
			def_data = {
				'email':user.email,
				'address':prof.address,
				'name':prof.name,
				'phone':prof.phone,
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
		'total':total,
	}
	###
	return render(request, 'cart_order.html', data)
