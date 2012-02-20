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

from collage.common.helpers import CropImg
from collage.common.models import Frames, Packaging
from collage.mosaic.models import MosaicSize, Mosaic, TYPE_CHOISES, EFFECT_CHOISES
from collage.mosaic.forms import MosaicForm, UploadForm, CreateForm, SIZE_INIT
from collage.mosaic.decorators import reload

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

@reload()
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

@reload()
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
				qty = 1			
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
	json = {'error':1, 'message':'Нет такого изображения'}
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
			p = p[0]
			###
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
			json['message'] = 'Изображение удалено'
			json['error'] = 0
	###
	return HttpResponse(simplejson.dumps(json))

@reload()
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
				form.save()
				###
				messages.success(request, 'Параметры изображения сохранены')
				"""if send_data['to_cart'] == 0:
					messages.success(request, 'Параметры изображения сохранены')
				elif send_data['to_cart'] == 1:
					if request.CART.set(file_id, 2, True):
						messages.success(request, 'Параметры сохранены, а изображение добавлено в корзину')
					else:
						messages.success(request, 'Параметры сохранены, а изображение уже ранее было добавлено в корзину')"""
			else:
				messages.error(request, 'Не верно выбраны параметры изображения')
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
	json = {'error':1, 'message':"Ошибка: Не найдена опция", 'url':'',}
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
					json = {'error':0, 'message':'Файл успешно загружен', 'url':url,}
				else:
					json = {'error':1, 'message':"Ошибка: %s" % img.error, 'url':'',}
			else:
				json = {'error':1, 'message':"Ошибка: Ошибка отправки исходных данных", 'url':'',}
		else:
			json = {'error':1, 'message':"Ошибка: Загрузите правильное изображение", 'url':'',}
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

'''
import datetime
import random

from PIL import Image
from md5 import md5

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, HttpResponseBadRequest
from django.utils import simplejson
from django.core.cache import cache
from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import messages

from collage.common.helpers import CropImg, CookieMosaicOption, BaseImg
from collage.mosaic.models import MosaicPrice, MosaicOption, SIZE_CHOISES
from collage.mosaic.forms import MosaicOptionForm, MosaicUploadForm
from collage.crop.models import Frames, Packaging
from collage.mosaic.settings import *

class DataImg(object):

	def save_nobody(self, img=None, char_id='', t_size=(), eff=1):
		img.save("%s%s%s.%s" % (FILES_DIR, DIR_NOBODY, char_id, SAVE_IMG_EXT))
		img.thumb("%s%s%s%s.%s" % (FILES_DIR, DIR_NOBODY, DIR_SMALLTHUMBS, char_id, SAVE_IMG_EXT))
		###
		if eff == 3: img.sepia()
		if eff == 2: img.BlackWhite()
		###
		img.resize_only(t_size[0], t_size[1])
		###
		img.save("%s%s%s%s.%s" % (FILES_DIR, DIR_NOBODY, DIR_THUMBS, char_id, SAVE_IMG_EXT))

	def save_auth(self, img=None, char_id='', t_size=(), eff=1):
		n = datetime.datetime.now()
		###
		dir_date = ''.join([str(n.year), '/', '%02d%02d/' % (n.month, n.day)])
		###
		pth_file = ''.join([FILES_DIR, DIR_AUTH, dir_date])
		pth_change = ''.join([pth_file, DIR_CHANGE])
		pth_thumb = ''.join([pth_file, DIR_THUMBS])
		pth_smallthumb = ''.join([pth_file, DIR_SMALLTHUMBS])
		###
		if not os.path.isdir(pth_file):
			os.makedirs(pth_file)
			os.makedirs(pth_change)
			os.makedirs(pth_thumb)
			os.makedirs(pth_smallthumb)
		###
		img.save("%s%s.%s" % (pth_file, char_id, SAVE_IMG_EXT))
		img.thumb("%s%s.%s" % (pth_smallthumb, char_id, SAVE_IMG_EXT))
		###
		if eff == 3: img.sepia()
		if eff == 2: img.BlackWhite()
		###
		img.resize_only(t_size[0], t_size[1])
		###
		img.save("%s%s.%s" % (pth_thumb, char_id, SAVE_IMG_EXT))
		###
		return dir_date

	def del_auth(self, file_id='', pth=''):
		pth_file = ''.join([PATH_PJT, pth])
		pth_change = ''.join([pth_file, DIR_CHANGE])
		pth_thumb = ''.join([pth_file, DIR_THUMBS])
		pth_smallthumb = ''.join([pth_file, DIR_SMALLTHUMBS])
		###
		f = ''.join([pth_file, file_id, '.', SAVE_IMG_EXT])
		if os.path.isfile(f): os.remove(f)
		###
		f = ''.join([pth_change, file_id, '.', SAVE_IMG_EXT])
		if os.path.isfile(f): os.remove(f)
		###
		f = ''.join([pth_thumb, file_id, '.', SAVE_IMG_EXT])
		if os.path.isfile(f): os.remove(f)
		###
		f = ''.join([pth_smallthumb, file_id, '.', SAVE_IMG_EXT])
		if os.path.isfile(f): os.remove(f)

	def del_nobody(self, file_id=''):
		f = ''.join([FILES_DIR, DIR_NOBODY, file_id, '.', SAVE_IMG_EXT])
		if os.path.isfile(f): os.remove(f)
		###
		f = ''.join([FILES_DIR, DIR_NOBODY, DIR_THUMBS, file_id, '.', SAVE_IMG_EXT])
		if os.path.isfile(f): os.remove(f)
		###
		f = ''.join([FILES_DIR, DIR_NOBODY, DIR_SMALLTHUMBS, file_id, '.', SAVE_IMG_EXT])
		if os.path.isfile(f): os.remove(f)
		###
		f = ''.join([FILES_DIR, DIR_NOBODY, DIR_CHANGE, file_id, '.', SAVE_IMG_EXT])
		if os.path.isfile(f): os.remove(f)

	def effect_auth_file(self, mo=None, eff=1, table_type=1, i=0):
		ret = False
		###
		pth_file = ''.join([PATH_PJT, mo.pth])
		pth_thumb = ''.join([pth_file, DIR_THUMBS])
		###
		k = 'f_%s' % (i,)
		###
		char_id = getattr(mo, k)
		###
		if not char_id == '':
			f = ''.join([pth_file, char_id, '.', SAVE_IMG_EXT])
			f_t = ''.join([pth_thumb, char_id, '.', SAVE_IMG_EXT])
			###
			if os.path.isfile(f):
				self.url[k] = ''.join([mo.pth, DIR_THUMBS, char_id, '.', SAVE_IMG_EXT, '?r=', str(random.random())])
				###
				img = CropImg(f, None, MIN_W, MIN_H, MIN_DPI)
				###
				if eff == 3: img.sepia()
				if eff == 2: img.BlackWhite()
				###
				if table_type == 1:
					img.resize_only(TYPE_SIZE_1[i][0], TYPE_SIZE_1[i][1])
				if table_type == 2:
					img.resize_only(TYPE_SIZE_2[i][0], TYPE_SIZE_2[i][1])
				if table_type == 3:
					img.resize_only(TYPE_SIZE_3[i][0], TYPE_SIZE_3[i][1])
				###
				img.save(f_t)
				###
				ret = True
		else:
			self.url[k] = ''
		###
		return ret

	def effect_nobody_file(self, row={}, eff=1, table_type=1, i=0):
		ret = False
		###
		k = 'f_%s' % (i,)
		###
		char_id = row[k]
		###
		if not char_id == '':
			f = ''.join([FILES_DIR, DIR_NOBODY, char_id, '.', SAVE_IMG_EXT])
			f_t = ''.join([FILES_DIR, DIR_NOBODY, DIR_THUMBS, char_id, '.', SAVE_IMG_EXT])
			###
			if os.path.isfile(f):
				self.url[k] = ''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_NOBODY, DIR_THUMBS, char_id, '.', SAVE_IMG_EXT, '?r=', str(random.random())])
				###
				img = CropImg(f, None, MIN_W, MIN_H, MIN_DPI)
				###
				if eff == 3: img.sepia()
				if eff == 2: img.BlackWhite()
				###
				if table_type == 1:
					img.resize_only(TYPE_SIZE_1[i][0], TYPE_SIZE_1[i][1])
				if table_type == 2:
					img.resize_only(TYPE_SIZE_2[i][0], TYPE_SIZE_2[i][1])
				if table_type == 3:
					img.resize_only(TYPE_SIZE_3[i][0], TYPE_SIZE_3[i][1])
				###
				img.save(f_t)
				###
				ret = True
		else:
			self.url[k] = ''
		###
		return ret

	def effect_auth(self, mo=None, eff=1, table_type=1):
		ret = False
		###
		self.url = {}
		###
		for i in xrange(9):
			now_ret = self.effect_auth_file(mo, eff, table_type, i)
			###
			if not ret and now_ret:
				ret = now_ret
		###
		return ret

	def effect_nobody(self, row={}, eff=1, table_type=1):
		ret = False
		###
		self.url = {}
		###
		for i in xrange(9):
			now_ret = self.effect_nobody_file(row, eff, table_type, i)
			###
			if not ret and now_ret:
				ret = now_ret
		###
		return ret

def choise(request):
	user = request.user
	###
	thumbs = []
	###
	if (user.is_authenticated() and user.is_active):
		if MosaicOption.objects.filter(user=user.id).exists():
			thumbs = MosaicOption.objects.filter(user=user.id)
	else:
		cmo = CookieMosaicOption()
		###
		thumbs = cmo.get_data(request)
	###
	data = {
		'thumbs':thumbs,
	}
	###
	return render(request, 'mosaic_choise.html', data)

def option(request):
	table_type = int(request.GET.get('type', 1))
	###
	if table_type not in (1, 2, 3,):
		table_type = 1
	###
	user = request.user
	###
	form = MosaicOptionForm()
	cmo = CookieMosaicOption()
	###
	opt_id = int(request.GET.get('opt_id', 0))
	###
	if (user.is_authenticated() and user.is_active):
		opts = MosaicOption.objects.filter(user=user.id)
		###
		if MosaicOption.objects.filter(user=user.id, opt_id=opt_id).exists():
			row = MosaicOption.objects.get(user=user.id, opt_id=opt_id)
		else:
			row = form.getDefObj(MosaicOption().newId(user), table_type)
	else:
		opts = cmo.get_data(request)
		###
		row = form.find(opts, opt_id)
		###
		if row is None:
			row = form.getDefRow(len(opts)+1, table_type)
	###
	if request.method == 'POST':
		form = MosaicOptionForm(request.POST)
		###
		if form.is_valid():
			send_data = form.cleaned_data
			###
			if (user.is_authenticated() and user.is_active):
				if MosaicOption.objects.filter(user=user.id, opt_id=send_data['opt_id']).exists():
					mo = MosaicOption.objects.get(user=user.id, opt_id=send_data['opt_id'])
					###
					mo.qty = send_data['qty']
					mo.table_size = send_data['table_size']
					mo.effect = send_data['effect']
					mo.frame = send_data['frame']
					mo.packaging = send_data['packaging']
					###
					mo.save()
					###
					if send_data['to_cart'] == 0:
						messages.success(request, 'Параметры изображения сохранены')
					elif send_data['to_cart'] == 1:
						if request.CART.set(send_data['opt_id'], 3, True):
							messages.success(request, 'Параметры сохранены, а изображение добавлено в корзину')
						else:
							messages.success(request, 'Параметры сохранены, а изображение уже ранее было добавлено в корзину')
				###
				return HttpResponseRedirect('/mosaic/option?opt_id=%s' % (send_data['opt_id'],))
			else:
				row['qty'] = send_data['qty']
				row['table_size'] = send_data['table_size']
				row['effect'] = send_data['effect']
				row['frame'] = send_data['frame'].id
				row['packaging'] = send_data['packaging'].id
				###
				for o in opts:
					if o['opt_id'] == send_data['opt_id']:
						o = row
						###
						if send_data['to_cart'] == 0:
							messages.success(request, 'Параметры изображения сохранены')
						elif send_data['to_cart'] == 1:
							if request.CART.set(send_data['opt_id'], 3, False):
								messages.success(request, 'Параметры сохранены, а изображение добавлено в корзину')
							else:
								messages.success(request, 'Параметры сохранены, а изображение уже ранее было добавлено в корзину')
						###
						break
				###
				resp = HttpResponseRedirect('/mosaic/option?opt_id=%s' % (send_data['opt_id'],))
				###
				return cmo.set_data(resp, opts)
		else:
			messages.error(request, 'Не верно выбраны параметры изображения')
	###
	if (user.is_authenticated() and user.is_active):
		DataImg().effect_auth(row, row.effect, row.table_type)
		###
		row = form.getDataRow(row)
	else:
		DataImg().effect_nobody(row, row['effect'], row['table_type'])
	###
	form = MosaicOptionForm(row)
	###
	param = {
		'opts':opts,
		'row':row,
		'form':form,
		'SIZE_CHOISES':SIZE_CHOISES,
		'MosaicPrice':MosaicPrice.objects.all(),
	}
	###
	return render(request, 'mosaic_option.html', param)

def upload_file(request):
	set_cook = False
	###
	if request.method == 'POST':
		form = MosaicUploadForm(request.POST, request.FILES)
		###
		if form.is_valid():
			user = request.user
			###
			send_data = form.cleaned_data
			###
			img = CropImg(request.FILES, 'file', MIN_W, MIN_H, MIN_DPI)
			###
			if img.is_valid():
				char_id = md5(''.join([SECRET_KEY[8], str(datetime.datetime.now())])).hexdigest()
				###
				table_type = int(send_data['table_type'])
				div_id = int(send_data['div_id'])
				###
				if table_type == 1:
					t_size = TYPE_SIZE_1[div_id]
				if table_type == 2:
					t_size = TYPE_SIZE_2[div_id]
				if table_type == 3:
					t_size = TYPE_SIZE_3[div_id]
				###
				if (user.is_authenticated() and user.is_active):
					dir_date = DataImg().save_auth(img, char_id, t_size, int(send_data['img_effect']))
					###
					if MosaicOption.objects.filter(user=user.id, opt_id=send_data['opt_id']).exists():
						mo = MosaicOption.objects.get(user=user.id, opt_id=send_data['opt_id'])
					else:
						pth = ''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_AUTH, dir_date])
						###
						mo = MosaicOption.objects.create(
							table_type = table_type,
							ext = SAVE_IMG_EXT,
							pth = ''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_AUTH, dir_date]),
							user = user,
							opt_id = send_data['opt_id'],
							effect = send_data['img_effect'],
							frame = Frames.objects.get(pk=1),
							packaging = Packaging.objects.get(pk=1)
						)
					###
					pth = ''.join([mo.pth, DIR_THUMBS])
					###
					for i in xrange(9):
						if div_id == i: mo.__setattr__('f_%s' % (i,), char_id)
					###
					mo.save()
				else:
					frm = MosaicOptionForm()
					cmo = CookieMosaicOption()
					###
					DataImg().save_nobody(img, char_id, t_size, int(send_data['img_effect']))
					###
					pth = ''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_NOBODY, DIR_THUMBS,])
					###
					opts = cmo.get_data(request)
					###
					opt_id = int(send_data['opt_id'])
					###
					row = frm.find(opts, opt_id)
					###
					new_row = False
					###
					if row is None:
						new_row = True
						###
						row = frm.getDefRow(opt_id, table_type)
					###
					row['f_%s' % send_data['div_id']] = char_id
					row['effect'] = send_data['img_effect']
					###
					set_cook = True
				###
				json = {'error':0, 'message':'Файл успешно загружен', 'url':''.join([pth, char_id, '.', SAVE_IMG_EXT,]), 'pth':pth, 'div_id':div_id, 'file':char_id,}
			else:
				json = {'error':1, 'message':"Ошибка: %s" % img.error, 'file':'',}
		else:
			json = {'error':1, 'message':"Ошибка: Загрузите правильное изображение", 'file':'',}
	###
	if set_cook:
		if new_row:
			opts.append(row)
		else:
			for o in opts:
				if o['opt_id'] == opt_id:
					o = row
					###
					break
		###
		resp = HttpResponse(simplejson.dumps(json))
		###
		return cmo.set_data(resp, opts)
	else:
		return HttpResponse(simplejson.dumps(json))

def delete_file(request):
	json = {'error':1, 'message':'Нет такой мозаики'}
	###
	set_cook = False
	###
	if request.is_ajax():
		user = request.user
		###
		form = MosaicOptionForm()
		cmo = CookieMosaicOption()
		di = DataImg()
		###
		opt_id = int(request.GET.get('opt_id', 0))
		###
		if (user.is_authenticated() and user.is_active):
			opts = MosaicOption.objects.filter(user=user.id)
			###
			if MosaicOption.objects.filter(user=user.id, opt_id=opt_id).exists():
				row = MosaicOption.objects.get(user=user.id, opt_id=opt_id)
				###
				for i in xrange(9):
					di.del_auth(getattr(row, 'f_%s' % (i,)), row.pth)
				###
				MosaicOption.objects.filter(user=user.id, opt_id=opt_id).delete()
				###
				json['message'] = 'Изображение удалено'
				json['error'] = 0
		else:
			opts = cmo.get_data(request)
			###
			row = form.find(opts, opt_id)
			###
			if row is not None:
				for i in xrange(9):
					di.del_nobody(row['f_%s' % (i,)])
				###
				set_cook = True
				###
				json['message'] = 'Изображение удалено'
				json['error'] = 0
			###
			for i in opts:
				if i['opt_id'] == opt_id:
					opts.remove(i)
					###
					set_cook = True
					###
					break
	###
	if set_cook:
		resp = HttpResponse(simplejson.dumps(json))
		###
		return cmo.set_data(resp, opts)
	else:
		return HttpResponse(simplejson.dumps(json))

def effect(request, file_id=''):
	user = request.user
	set_eff = False
	json = {'error':1, 'message':'Ошибка данных',}
	###
	eff = int(request.GET.get('eff', 1))
	###
	if eff not in (1, 2, 3):
		eff = 1
	###
	table_type = int(request.GET.get('type', 0))
	###
	if table_type in (1, 2, 3,):
		opt_id = int(request.GET.get('opt_id', 0))
		###
		di = DataImg()
		###
		if (user.is_authenticated() and user.is_active):
			if MosaicOption.objects.filter(user=user.id, opt_id=opt_id).exists():
				mo = MosaicOption.objects.get(user=user.id, opt_id=opt_id)
				###
				pth_file = ''.join([PATH_PJT, mo.pth])
				pth_thumb = ''.join([pth_file, DIR_THUMBS])
				###
				set_eff = di.effect_auth(mo, eff, table_type)
		else:
			opts = CookieMosaicOption().get_data(request)
			###
			row = MosaicOptionForm().find(opts, opt_id)
			###
			if row is not None:
				set_eff = di.effect_nobody(row, eff, table_type)
		###
		if set_eff:
			json = {'error':0, 'message':'Эффект установлен',}
			###
			for i in xrange(9):
				k = 'f_%s' % (i,)
				###
				json[k] = di.url[k]
	###
	return HttpResponse(simplejson.dumps(json))
'''
