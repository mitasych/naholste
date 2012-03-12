# -*- coding: utf-8 -*-

import datetime

from md5 import md5

from collage.crop.settings import *
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages

from collage.gallery.models import Album, Images

from collage.common.helpers import CropImg
from collage.crop.views import DataImg
from collage.crop.models import Crop, CropSize

from collage.puzzle.views import DataImg as PuzzleDataImg
from collage.puzzle.models import PuzzleSize, Puzzle

import Image

from collage.common.models import Stretch

STRETCH_INIT = Stretch.objects.get(defrow=True)
SIZE_INIT = CropSize.objects.get(defsize=True)

def albums(request):
	data = {
		'albums':Album.objects.all(),
		'MEDIA_URL':MEDIA_URL,
	}
	###
	return render(request, 'gallery_albums.html', data)

def images(request):
	try:
		album_id = int(request.GET.get('album', 0))
	except:
		return HttpResponseRedirect(reverse('gallery.views.albums'))
	###
	data = {
		'images':Images.objects.filter(album = album_id),
		'MEDIA_URL':MEDIA_URL,
	}
	###
	return render(request, 'gallery_images.html', data)



def to_crop(request):
	user = request.user
	auth = (user.is_authenticated() and user.is_active) and True or False
	###
	img = CropImg(''.join([MEDIA_ROOT, request.GET.get('img', 0)]), None, MIN_W, MIN_H, MIN_DPI)
	#img = Image.open(''.join([MEDIA_ROOT, request.GET.get('img', 0)]))
	###
	di = DataImg()
	###
	char_id = md5(''.join([SECRET_KEY[8], str(datetime.datetime.now())])).hexdigest()
	###
	di.save(obj=img, img=char_id)
	###
	p = Crop.objects.create(
		img = char_id,
		img_stretch = STRETCH_INIT,
		img_type = 1,
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
	###
	return HttpResponseRedirect(''.join(['/crop/option/?id=', str(p.id)]))