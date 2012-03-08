# -*- coding: utf-8 -*-

import datetime
import random

from md5 import md5

from collage.mosaic.settings import *
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

from collage.common.decorators import reload
from collage.common.helpers import CropImg
from collage.common.models import Frames, Packaging
from collage.mosaic.models import MosaicSize, Mosaic, TYPE_CHOISES, EFFECT_CHOISES
from collage.mosaic.forms import MosaicForm, UploadForm, CreateForm, SIZE_INIT

class DataImg(object):

	f = ''.join([FILES_DIR, '%s.', IMG_EXT])
	t = ''.join([FILES_DIR, DIR_THUMBS, '%s.', IMG_EXT])
	s = ''.join([FILES_DIR, DIR_SMALLTHUMBS, '%s.', IMG_EXT])

	def delImg(self, img=''):
		f = self.f % img
		if os.path.isfile(f): os.remove(f)
		###
		f = self.t % img
		if os.path.isfile(f): os.remove(f)
		###
		f = self.s % img
		if os.path.isfile(f): os.remove(f)

	def save(self, obj=None, img='', w=0, h=0):
		obj.save(self.f % img)
		obj.thumb(self.s % img)
		obj.resize_only(w, h)
		obj.save(self.t % img)

	def effect(self, img='', eff=1, w=0, h=0):
		ret = False
		###
		f = self.f % img
		t = self.t % img
		###
		self.url = ''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_THUMBS, img, '.', IMG_EXT, '?r=', str(random.random())])
		###
		if os.path.isfile(t):
			obj = CropImg(f, None, MIN_W, MIN_H, MIN_DPI)
			###
			if eff == 3:
				obj.sepia()
			###
			if eff == 2:
				obj.BlackWhite()
			###
			obj.resize_only(w, h)
			obj.save(t)
			###
			ret = True
		###
		return ret

@reload(Mosaic)
def choise(request):
	user = request.user
	auth = (user.is_authenticated() and user.is_active) and True or False
	###
	q = auth and Q(user=user.id) or Q(nouser=request.NOUSER.get())
	###
	data = {
		'form':CreateForm(),
		'thumbs':list(Mosaic.objects.filter(q)),
	}
	###
	return render(request, 'mosaic_choise.html', data)

@reload(Mosaic)
def create(request):
	if request.method == 'POST':
		form = CreateForm(request.POST)
		###
		if form.is_valid():
			user = request.user
			auth = (user.is_authenticated() and user.is_active) and True or False
			###
			send_data = form.cleaned_data
			###
			if int(send_data['table_type']) == 1:
				s = MosaicSize.objects.get(pk=1)
			if int(send_data['table_type']) == 2:
				s = MosaicSize.objects.get(pk=5)
			if int(send_data['table_type']) == 3:
				s = MosaicSize.objects.get(pk=9)
			###
			p = Mosaic.objects.create(
				table_type = send_data['table_type'],
				img_size = s,
				img_effect = 1,
				qty = 1,
				status = False
			)
			###
			if auth:
				p.user = user
			else:
				p.nouser = request.NOUSER.get()
			###
			p.save()
			###
			return HttpResponseRedirect('/mosaic/option?id=%s' % p.id)
	###
	return HttpResponseRedirect(reverse(REDIRECT))

def delete_file(request):
	json = {'error':1, 'message':u'Нет такого изображения'}
	###
	if request.is_ajax():
		try:
			opt_id = int(request.GET.get('id', 0))
		except:
			return HttpResponseRedirect(reverse(REDIRECT))
		###
		user = request.user
		auth = (user.is_authenticated() and user.is_active) and True or False
		###
		di = DataImg()
		###
		q = auth and Q(user=user.id, pk=opt_id) or Q(nouser=request.NOUSER.get(), pk=opt_id)
		###
		p = Mosaic.objects.filter(q)
		###
		if p.exists():
			p = Mosaic.objects.get(q)
			###
			if p.status:
				json['message'] = u'По изображениям сформирован заказ - удаление невозможно'
			else:
				if p.table_type == 1:
					len_size = 9
				if p.table_type == 2:
					len_size = 7
				if p.table_type == 3:
					len_size = 7
				###
				for i in xrange(len_size):
					v = getattr(p, 'f_%s' % i)
					###
					if not v == '':
						di.delImg(v)
				###
				p.delete()
				###
				json['message'] = u'Изображение удалено'
				json['error'] = 0
	###
	return HttpResponse(simplejson.dumps(json))

@reload(Mosaic)
def option(request):
	user = request.user
	auth = (user.is_authenticated() and user.is_active) and True or False
	di = DataImg()
	###
	try:
		opt_id = int(request.GET.get('id', 0))
	except:
		return HttpResponseRedirect(reverse(REDIRECT))
	###
	q = auth and Q(user=user.id, pk=opt_id) or Q(nouser=request.NOUSER.get(), pk=opt_id)
	qt = auth and Q(user=user.id) or Q(nouser=request.NOUSER.get())
	###
	p = Mosaic.objects.filter(q)
	###
	if p.exists():
		p = Mosaic.objects.get(q)
		###
		if request.method == 'POST':
			form = MosaicForm(request.POST, instance=p)
			###
			if form.is_valid():
				send_data = form.cleaned_data
				###
				form.save()
				###
				if send_data['to_cart'] == 0:
					messages.success(request, u'Параметры изображения сохранены')
				elif send_data['to_cart'] == 1:
					if request.CART.add(p.id, 3, auth):
						messages.success(request, u'Параметры сохранены, а изображение добавлено в корзину')
					else:
						messages.success(request, u'Параметры сохранены, а изображение уже ранее было добавлено в корзину')
					###
					return HttpResponseRedirect(reverse('cart.views.show'))
			else:
				messages.error(request, u'Не верно выбраны параметры изображения')
		else:
			form = MosaicForm(instance=p)
			###
			if p.table_type == 1:
				size = TYPE_SIZE_1
				len_size = 9
			if p.table_type == 2:
				size = TYPE_SIZE_2
				len_size = 7
			if p.table_type == 3:
				size = TYPE_SIZE_3
				len_size = 7
			###
			for i in xrange(len_size):
				v = getattr(p, 'f_%s' % i)
				###
				if not v == '':
					di.effect(v, p.img_effect, size[i][0], size[i][1])
	else:
		return HttpResponseRedirect(reverse(REDIRECT))
	###
	thumbs = list(Mosaic.objects.filter(qt))
	###
	data = {
		'form':form,
		'thumbs':thumbs,
		'dataType':TYPE_CHOISES,
		'dataEffect':EFFECT_CHOISES,
	}
	###
	return render(request, 'mosaic_option.html', data)

def upload_file(request):
	json = {'error':1, 'message':u"Ошибка: Не найдена опция", 'url':'',}
	###
	try:
		opt_id = int(request.GET.get('id', 0))
	except:
		return HttpResponseRedirect(reverse(REDIRECT))
	###
	if opt_id > 0 and request.method == 'POST':
		user = request.user
		auth = (user.is_authenticated() and user.is_active) and True or False
		###
		q = auth and Q(user=user.id, pk=opt_id) or Q(nouser=request.NOUSER.get(), pk=opt_id)
		###
		p = Mosaic.objects.filter(q)
		###
		if p.exists():
			p = Mosaic.objects.get(q)
			form = UploadForm(request.POST, request.FILES)
			###
			if form.is_valid():
				send_data = form.cleaned_data
				###
				img = CropImg(request.FILES, 'file', MIN_W, MIN_H, MIN_DPI)
				###
				if img.is_valid():
					di = DataImg()
					###
					char_id = md5(''.join([SECRET_KEY[8], str(datetime.datetime.now())])).hexdigest()
					###
					if p.table_type == 1:	size = TYPE_SIZE_1
					if p.table_type == 2:	size = TYPE_SIZE_2
					if p.table_type == 3:	size = TYPE_SIZE_3
					###
					send_data['div_id'] = int(send_data['div_id'])
					###
					di.save(obj=img, img=char_id, w=size[send_data['div_id']][0], h=size[send_data['div_id']][1])
					###
					send_data['effect'] = int(send_data['effect'])
					###
					if send_data['effect'] == 2 or send_data['effect'] == 3:
						di.effect(char_id, send_data['effect'], size[send_data['div_id']][0], size[send_data['div_id']][1])
					###
					setattr(p, 'f_%s' % send_data['div_id'], char_id)
					###
					p.save()
					###
					url = ''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_THUMBS, char_id, '.', IMG_EXT])
					###
					json = {'error':0, 'message':u'Файл успешно загружен', 'url':url,}
				else:
					json = {'error':1, 'message':u"Ошибка: %s" % img.error, 'url':'',}
			else:
				json = {'error':1, 'message':u"Ошибка: Ошибка отправки исходных данных", 'url':'',}
		else:
			json = {'error':1, 'message':u"Ошибка: Загрузите правильное изображение", 'url':'',}
	###
	return HttpResponse(simplejson.dumps(json))

def effect(request):
	user = request.user
	auth = (user.is_authenticated() and user.is_active) and True or False
	di = DataImg()
	json = {'error':1, 'message':u'Нет такого изображения'}
	ret = False
	###
	try:
		opt_id = int(request.GET.get('id', 0))
		effect = int(request.GET.get('eff', 1))
		###
		if not effect in [1, 2, 3]: ret = True
	except:
		ret = True
	###
	if ret: return HttpResponse(simplejson.dumps(json))
	###
	q = auth and Q(user=user.id, pk=opt_id) or Q(nouser=request.NOUSER.get(), pk=opt_id)
	###
	p = Mosaic.objects.filter(q)
	###
	if p.exists():
		p = Mosaic.objects.get(q)
		###
		if p.table_type == 1:
			size = TYPE_SIZE_1
			len_size = 9
		if p.table_type == 2:
			size = TYPE_SIZE_2
			len_size = 7
		if p.table_type == 3:
			size = TYPE_SIZE_3
			len_size = 7
		###
		for i in xrange(len_size):
			k = 'f_%s' % i
			v = getattr(p, k)
			###
			json[k] = ''
			###
			if not v == '':
				di.effect(v, effect, size[i][0], size[i][1])
				###
				json[k] = di.url
		###
		json['error'] = 0;
		json['message'] = u'Эффект установлен';
	###
	return HttpResponse(simplejson.dumps(json))
