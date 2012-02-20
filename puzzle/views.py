# -*- coding: utf-8 -*-
import datetime
import random

from md5 import md5

from collage.puzzle.settings import *
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
from collage.puzzle.models import PuzzleSize, Puzzle, Stretch, EFFECT_CHOISES
from collage.puzzle.forms import PuzzleForm, UploadForm, SIZE_INIT, STRETCH_INIT
from collage.puzzle.decorators import reload

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

	def save(self, obj=None, img=''):
		obj.save(self.f % img)
		obj.thumb(self.s % img)
		obj.resize(THUMB_W, THUMB_X)
		obj.save(self.t % img)

	def size(self, img=''):
		f = self.f % img
		t = self.t % img
		###
		sf = CropImg(f, None, MIN_W, MIN_H, MIN_DPI).getOriginSize()
		st = CropImg(t, None, MIN_W, MIN_H, MIN_DPI).getOriginSize()
		###
		return {
			'fw':sf[0],
			'fh':sf[1],
			'tw':st[0],
			'th':st[1],
		}

	def effect(self, img='', eff=1):
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
			obj.resize(THUMB_W, THUMB_X)
			obj.save(t)
			###
			ret = True
		###
		return ret

@reload()
def upload(request):
	user = request.user
	auth = (user.is_authenticated() and user.is_active) and True or False
	###
	q = auth and Q(user=user.id) or Q(nouser=request.NOUSER.get())
	###
	data = {
		'form':UploadForm(),
		'thumbs':list(Puzzle.objects.filter(q)),
	}
	###
	return render(request, 'puzzle_upload.html', data)

def upload_file(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		###
		if form.is_valid():
			user = request.user
			auth = (user.is_authenticated() and user.is_active) and True or False
			###
			img = CropImg(request.FILES, 'file', MIN_W, MIN_H, MIN_DPI)
			###
			if img.is_valid():
				di = DataImg()
				###
				char_id = md5(''.join([SECRET_KEY[8], str(datetime.datetime.now())])).hexdigest()
				###
				di.save(obj=img, img=char_id)
				###
				p = Puzzle.objects.create(
					img = char_id,
					img_stretch = STRETCH_INIT,
					img_size = SIZE_INIT,
					img_effect = 1,
					qty = 1,
					x1 = 0,
					y1 = 0,
					x2 = 0,
					y2 = 0
				)
				###
				if auth:
					p.user = user
				else:
					p.nouser = request.NOUSER.get()
				###
				p.save()
				###
				json = {'error':0, 'message':'Файл успешно загружен', 'id':p.id,}
			else:
				json = {'error':1, 'message':"Ошибка: %s" % img.error, 'id':'',}
		else:
			json = {'error':1, 'message':"Ошибка: Загрузите правильное изображение", 'id':'',}
	###
	return HttpResponse(simplejson.dumps(json))

def delete_file(request):
	json = {'error':1, 'message':'Нет такого изображения'}
	###
	if request.is_ajax():
		try:
			opt_id = int(request.GET.get('id', 0))
		except:
			return HttpResponseRedirect(reverse('puzzle.views.upload'))
		###
		user = request.user
		auth = (user.is_authenticated() and user.is_active) and True or False
		###
		di = DataImg()
		###
		q = auth and Q(user=user.id, pk=opt_id) or Q(nouser=request.NOUSER.get(), pk=opt_id)
		###
		p = Puzzle.objects.filter(q)
		###
		if p.exists():
			p = p[0]
			di.delImg(p.img)
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
	redirect = 'puzzle.views.upload'
	di = DataImg()
	###
	try:
		opt_id = int(request.GET.get('id', 0))
	except:
		return HttpResponseRedirect(reverse(redirect))
	###
	q = auth and Q(user=user.id, pk=opt_id) or Q(nouser=request.NOUSER.get(), pk=opt_id)
	qt = auth and Q(user=user.id) or Q(nouser=request.NOUSER.get())
	###
	p = Puzzle.objects.filter(q)
	###
	if p.exists():
		p = Puzzle.objects.get(q)
		###
		if request.method == 'POST':
			form = PuzzleForm(request.POST, instance=p)
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
			form = PuzzleForm(instance=p)
			di.effect(p.img, p.img_effect)
	else:
		return HttpResponseRedirect(reverse(redirect))
	###
	thumbs = list(Puzzle.objects.filter(qt))
	size = di.size(p.img)
	###
	data = {
		'form':form,
		'thumbs':thumbs,
		'src':''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_THUMBS, p.img, '.', IMG_EXT]),
		'img_w':size['tw'],
		'img_h':size['th'],
		'origin_w':size['fw'],
		'origin_h':size['fh'],
		'dataStretch':Stretch.objects.all(),
		'dataEffect':EFFECT_CHOISES,
	}
	###
	return render(request, 'puzzle_option.html', data)

def effect(request):
	user = request.user
	auth = (user.is_authenticated() and user.is_active) and True or False
	di = DataImg()
	json = {'error':1, 'message':u'Нет такого изображения', 'file':''}
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
	p = Puzzle.objects.filter(q)
	###
	if p.exists():
		p = Puzzle.objects.get(q)
		###
		di.effect(p.img, effect)
		###
		json['error'] = 0;
		json['message'] = u'Эффект установлен';
		json['file'] = di.url;
	###
	return HttpResponse(simplejson.dumps(json))

