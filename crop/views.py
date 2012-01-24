# -*- coding: utf-8 -*-

import datetime
import random

from PIL import Image
from md5 import md5

from collage.crop.settings import *
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, HttpResponseBadRequest
from django.utils import simplejson
from django.core.cache import cache
from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from collage.common.helpers import CropImg, CookieListFiles, CookieListOptions
from collage.crop.models import CropPrice, Files, OptionFiles, Frames, Packaging
from collage.crop.forms import UploadForm, OptionForm

class DataImg(object):

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

	def save_nobody(self, img=None, char_id=''):
		img.save("%s%s%s.%s" % (FILES_DIR, DIR_NOBODY, char_id, SAVE_IMG_EXT))
		img.thumb("%s%s%s%s.%s" % (FILES_DIR, DIR_NOBODY, DIR_SMALLTHUMBS, char_id, SAVE_IMG_EXT))
		###
		img.resize(THUMB_W, THUMB_X)
		###
		img.save("%s%s%s%s.%s" % (FILES_DIR, DIR_NOBODY, DIR_THUMBS, char_id, SAVE_IMG_EXT))

	def save_auth(self, img=None, char_id=''):
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
		img.resize(THUMB_W, THUMB_X)
		###
		img.save("%s%s.%s" % (pth_thumb, char_id, SAVE_IMG_EXT))
		###
		return dir_date

	def effect_auth(self, char_id='', pth='', eff=1):
		ret = False
		###
		pth_file = ''.join([PATH_PJT, pth])
		pth_thumb = ''.join([pth_file, DIR_THUMBS])
		###
		f = ''.join([pth_file, char_id, '.', SAVE_IMG_EXT])
		f_t = ''.join([pth_thumb, char_id, '.', SAVE_IMG_EXT])
		###
		self.url = ''.join([pth, DIR_THUMBS, char_id, '.', SAVE_IMG_EXT, '?r=', str(random.random())])
		###
		if os.path.isfile(f):
			img = CropImg(f, None, MIN_W, MIN_H, MIN_DPI)
			###
			size = img.getOriginSize()
			###
			self.origin_w = size[0]
			self.origin_h = size[1]
			###
			if eff == 3: img.sepia()
			if eff == 2: img.BlackWhite()
			###
			img.resize(THUMB_W, THUMB_X)
			###
			img.save(f_t)
			###
			size = img.getOriginSize()
			###
			self.w = size[0]
			self.h = size[1]
			###
			ret = True
		###
		return ret

	def effect_nobody(self, char_id='', eff=1):
		ret = False
		###
		f = ''.join([FILES_DIR, DIR_NOBODY, char_id, '.', SAVE_IMG_EXT])
		f_t = ''.join([FILES_DIR, DIR_NOBODY, DIR_THUMBS, char_id, '.', SAVE_IMG_EXT])
		###
		self.url = ''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_NOBODY, DIR_THUMBS, char_id, '.', SAVE_IMG_EXT, '?r=', str(random.random())])
		###
		if os.path.isfile(f):
			img = CropImg(f, None, MIN_W, MIN_H, MIN_DPI)
			###
			size = img.getOriginSize()
			###
			self.origin_w = size[0]
			self.origin_h = size[1]
			###
			if eff == 3: img.sepia()
			if eff == 2: img.BlackWhite()
			###
			img.resize(THUMB_W, THUMB_X)
			###
			img.save(f_t)
			###
			size = img.getOriginSize()
			###
			self.w = size[0]
			self.h = size[1]
			###
			ret = True
		###
		return ret

class DataOpt(object):

	def save_opt(self, row, data):
		if type(data['frame']).__name__ == 'int':
			frame = Frames.objects.get(pk=data['frame'])
		else:
			frame = data['frame']
		###
		if type(data['packaging']).__name__ == 'int':
			packaging = Packaging.objects.get(pk=data['packaging'])
		else:
			packaging = data['packaging']
		###
		OptionFiles(
			file = row,
			img_stretch = data['img_stretch'],
			img_type = data['img_type'],
			img_size = data['img_size'],
			img_effect = data['img_effect'],
			qty = data['qty'],
			frame = frame,
			packaging = packaging,
			x1 = data['x1'],
			y1 = data['y1'],
			x2 = data['x2'],
			y2 = data['y2'],
		).save()

def upload(request):
	user = request.user
	###
	thumbs = []
	###
	if (user.is_authenticated() and user.is_active):
		if Files.objects.filter(user=user.id).exists():
			thumbs = Files.objects.filter(user=user.id)
	else:
		clf = CookieListFiles()
		data = clf.get_data(request)
		###
		thumbs = Files().getListCookie(data)
	###
	form = UploadForm()
	###
	data = {
		'form':form,
		'thumbs':thumbs,
	}
	###
	return render(request, 'crop_upload.html', data)

def reload(request):
	user = request.user
	###
	if (user.is_authenticated() and user.is_active):
		clf = CookieListFiles()
		data = clf.get_data(request)
		thumbs = Files().getListCookie(data)
		###
		clo = CookieListOptions()
		opts = clo.get_data(request)
		###
		if len(thumbs) > 0:
			for f in thumbs:
				if not Files.objects.filter(char_id=f['char_id']).exists():
					origin = "%s%s%s.%s" % (FILES_DIR, DIR_NOBODY, f['char_id'], SAVE_IMG_EXT)
					###
					if os.path.isfile(origin):
						img = CropImg(origin, None, MIN_W, MIN_H, MIN_DPI)
						###
						dir_date = DataImg().save_auth(img, f['char_id'])
						###
						new_f = Files(
							char_id=f['char_id'],
							user=user,
							ext=SAVE_IMG_EXT,
							pth=''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_AUTH, dir_date])
						)
						###
						new_f.save()
						###
						DataImg().del_nobody(f['char_id'])
						###
						for o in opts:
							if f['char_id'] == o['char_id']:
								DataOpt().save_opt(new_f, o)
								###
								break
			###
			messages.success(request, 'Изображения скопированы в ваш профиль')
			###
			resp = HttpResponseRedirect(reverse('crop.views.upload'))
			###
			clf.set_data(resp, [])
			clo.set_data(resp, [])
			###
			return resp

def upload_file(request):
	set_cook = False
	###
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		###
		if form.is_valid():
			user = request.user
			###
			img = CropImg(request.FILES, 'file', MIN_W, MIN_H, MIN_DPI)
			###
			if img.is_valid():
				char_id = md5(''.join([SECRET_KEY[8], str(datetime.datetime.now())])).hexdigest()
				###
				if (user.is_authenticated() and user.is_active):
					dir_date = DataImg().save_auth(img, char_id)
					###
					Files(
						char_id=char_id,
						user=user,
						ext=SAVE_IMG_EXT,
						pth=''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_AUTH, dir_date])
					).save()
				else:
					DataImg().save_nobody(img, char_id)
					###
					set_cook = True
				###
				json = {'error':0, 'message':'Файл успешно загружен', 'file':char_id,}
			else:
				json = {'error':1, 'message':"Ошибка: %s" % img.error, 'file':'',}
		else:
			json = {'error':1, 'message':"Ошибка: Загрузите правильное изображение", 'file':'',}
	###
	if set_cook:
		clf = CookieListFiles()
		thumbs = clf.get_data(request)
		###
		thumbs.append(char_id)
		###
		resp = HttpResponse(simplejson.dumps(json))
		###
		return clf.set_data(resp, thumbs)
	else:
		return HttpResponse(simplejson.dumps(json))

def delete_file(request, file_id=''):
	json = {'error':1, 'message':'Нет такого изображения'}
	###
	set_cook = False
	###
	if request.is_ajax():
		user = request.user
		###
		if (user.is_authenticated() and user.is_active):
			if Files.objects.filter(user=user.id, char_id=file_id).exists():
				row = Files.objects.get(user=user.id, char_id=file_id)
				###
				DataImg().del_auth(file_id, row.pth)
				###
				Files.objects.filter(user=user.id, char_id=file_id).delete()
				###
				json['message'] = 'Изображение удалено'
				json['error'] = 0
		else:
			clf = CookieListFiles()
			thumbs = clf.get_data(request)
			###
			if file_id in thumbs:
				set_cook = True
				###
				DataImg().del_nobody(file_id)
				###
				thumbs.remove(file_id)
				###
				json['message'] = 'Изображение удалено'
				json['error'] = 0
	###
	if set_cook:
		resp = HttpResponse(simplejson.dumps(json))
		###
		return clf.set_data(resp, thumbs)
	else:
		return HttpResponse(simplejson.dumps(json))
	
def option(request, file_id=''):
	user = request.user
	of = OptionForm()
	###
	thumbs = []
	###
	no_redirect = False
	###
	if (user.is_authenticated() and user.is_active):
		if Files.objects.filter(user=user.id, char_id=file_id).exists():
			row = Files.objects.get(user=user.id, char_id=file_id)
			###
			thumbs = Files.objects.filter(user=user.id)
			###
			no_redirect = True
			###
			ins = False
			###
			if OptionFiles.objects.filter(file=row).exists():
				opt = OptionFiles.objects.get(file=row)
				###
				ins = True
			else:
				opt = of.getDefObj(file_id)
	else:
		clf = CookieListFiles()
		clo = CookieListOptions()
		###
		data = clf.get_data(request)
		opts = clo.get_data(request)
		###
		thumbs = Files().getListCookie(data)
		###
		if file_id in data:
			no_redirect = True
			###
			row = Files().getRow(file_id)
			###
			not_found = True
			###
			for i in opts:
				if i['char_id'] == file_id:
					opt = i
					not_found = False
					break
			###
			if not_found:
				opt = of.getDefRow(file_id)
	###
	if no_redirect:
		if request.method == 'POST':
			form = OptionForm(request.POST)
			###
			if form.is_valid():
				send_data = form.cleaned_data
				###
				messages.success(request, 'Изображение добавлено в корзину покупок')
				###
				if (user.is_authenticated() and user.is_active):
					if ins:
						opt.img_stretch = send_data['img_stretch']
						opt.img_type = send_data['img_type']
						opt.img_size = send_data['img_size']
						opt.img_effect = send_data['img_effect']
						opt.qty = send_data['qty']
						opt.frame = send_data['frame']
						opt.packaging = send_data['packaging']
						opt.x1 = send_data['x1']
						opt.y1 = send_data['y1']
						opt.x2 = send_data['x2']
						opt.y2 = send_data['y2']
						###
						opt.save()
					else:
						DataOpt().save_opt(row, send_data)
					###
					return HttpResponseRedirect(reverse('crop.views.option', args=[file_id]))
				else:
					found = False
					###
					for f in opts:
						if f['char_id'] == file_id:
							f['img_stretch'] = send_data['img_stretch']
							f['img_type'] = send_data['img_type']
							f['img_size'] = send_data['img_size']
							f['img_effect'] = send_data['img_effect']
							f['qty'] = send_data['qty']
							f['frame'] = send_data['frame'].id
							f['packaging'] = send_data['packaging'].id
							f['x1'] = send_data['x1']
							f['y1'] = send_data['y1']
							f['x2'] = send_data['x2']
							f['y2'] = send_data['y2']
							###
							found = True
							###
							break
					###
					if not found:
						opts.append({
							'char_id':file_id,
							'img_stretch':send_data['img_stretch'],
							'img_type':send_data['img_type'],
							'img_size':send_data['img_size'],
							'img_effect':send_data['img_effect'],
							'qty':send_data['qty'],
							'frame':send_data['frame'].id,
							'packaging':send_data['packaging'].id,
							'qty':send_data['qty'],
							'x1':send_data['x1'],
							'y1':send_data['y1'],
							'x2':send_data['x2'],
							'y2':send_data['y2'],
						})
					###
					resp = HttpResponseRedirect(reverse('crop.views.option', args=[file_id]))
					###
					return clo.set_data(resp, opts)
			else:
				messages.error(request, 'Не верно выбраны параметры изображения')
		else:
			if (user.is_authenticated() and user.is_active):
				form = OptionForm(of.getDataRow(opt))
			else:
				form = OptionForm(opt)
		###
		di = DataImg()
		###
		if (user.is_authenticated() and user.is_active):
			di.effect_auth(file_id, row.pth, form['img_effect'].value())
		else:
			di.effect_nobody(file_id, form['img_effect'].value())
		###
		data = {
			'form':form,
			'thumbs':thumbs,
			'dir_thumbs':DIR_THUMBS,
			'row':row,
			'char_id':file_id,
			'img_w':di.w,
			'img_h':di.h,
			'origin_w':di.origin_w,
			'origin_h':di.origin_h,
			'nameStretch':form.getStretch(form['img_stretch'].value()),
			'nameType':form.getType(form['img_type'].value()),
			'nameSize':form.getSize(form['img_size'].value()),
			'nameEffect':form.getEffect(form['img_effect'].value()),
			'dataStretch':form.getStretchList(),
			'dataType':form.getTypeList(),
			'dataSize':form.getSizeList(),
			'dataEffect':form.getEffectList(),
		}
		###
		return render(request, 'crop_option.html', data)
	else:
		return HttpResponseRedirect(reverse('crop.views.upload'))

def effect(request, file_id=''):
	user = request.user
	set_eff = False
	json = {'error':1, 'message':'Нет такого изображения', 'file':''}
	###
	eff = int(request.GET.get('eff', 1))
	###
	if eff not in (1, 2, 3):
		eff = 1
	###
	di = DataImg()
	###
	if (user.is_authenticated() and user.is_active):
		if Files.objects.filter(user=user.id, char_id=file_id).exists():
			row = Files.objects.get(user=user.id, char_id=file_id)
			###
			pth_file = ''.join([PATH_PJT, row.pth])
			pth_thumb = ''.join([pth_file, DIR_THUMBS])
			###
			f = ''.join([pth_thumb, file_id, '.', SAVE_IMG_EXT])
			###
			if os.path.isfile(f):
				set_eff = di.effect_auth(file_id, row.pth, eff)
	else:
		clf = CookieListFiles()
		###
		data = clf.get_data(request)
		###
		thumbs = Files().getListCookie(data)
		###
		if file_id in data:
			f = ''.join([FILES_DIR, DIR_NOBODY, DIR_THUMBS, file_id, '.', SAVE_IMG_EXT])
			###
			if os.path.isfile(f):
				set_eff = di.effect_nobody(file_id, eff)
	###
	if set_eff:
		json = {'error':0, 'message':'Эффект установлен', 'file':di.url}
	###
	return HttpResponse(simplejson.dumps(json))
