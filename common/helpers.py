# -*- coding: utf-8 -*-
import datetime
import cPickle as pickle

from PIL import Image
from math import floor

class BaseImg(object):

	w = 300
	h = 200
	min_h = 100
	min_w = 100
	min_d = 50
	m = ('L', 'RGB',)
	img = None
	_is_valid = False
	error = ''
	convert = 'RGB'
	type_save = 'JPEG'
	quality = 100
	t_w = 100
	t_h = 70

	def __init__(self, min_w=None, min_h=None, min_d=None):
		if min_w is not None:
			self.min_w = min_w
		###
		if min_h is not None:
			self.min_h = min_h
		###
		if min_d is not None:
			self.min_d = min_d

	def getSize(self, w, h):
		if w > h:
			if w > self.w:
				r_h = h * float(self.w) / w
				r_w = self.w
			else:
				r_h = h
				r_w = w
		elif w < h:
			if h > self.h:
				r_w = w * float(self.h) / h
				r_h = self.h
			else:
				r_h = h
				r_w = w
		elif w == h:
			if w > self.w:
				r_w = self.w 
				r_h = self.w
			else:
				r_w = w
				r_h = w
		###
		return int(r_w), int(r_h)

	def getSizeCrop(self, wx=0, hx=0, wm=0, hm=0):
		r = float(self.img.size[0]) / float(self.img.size[1])
		rx = float(wx) / float(hx)
		###
		if ((wm == 0) or (hm == 0)):
			rm = rx
		else:
			rm = float(wm) / float(hm)
		###
		dx = 0
		dy = 0
		sx = 0
		sy = 0
		dw = 0
		dh = 0
		sw = 0
		sh = 0
		w = 0
		h = 0
		###
		if ((r > rx) and (r > rm)):
			w = wx
			h = hx
			sw = self.img.size[1] * rx
			sh = self.img.size[1]
			sx = floor((float(self.img.size[0]) - sw) / 2)
			dw = wx
			dh = hx
		elif ((r < rm) and (r < rx)):
			w = wx
			h = hx
			sh = floor(float(self.img.size[0]) / rx)
			sy = floor((float(self.img.size[1]) - sh) / 2)
			sw = self.img.size[0]
			dw = wx
			dh = hx
		elif ((r >= rx) and (r <= rm)):
			w = wx
			h = float(wx) / r
			dw = wx
			dh = float(wx) / r
			sw = self.img.size[0]
			sh = self.img.size[1]
		elif ((r <= rx) and (r >= rm)):
			w = hx * r;
			h = hx
			dw = hx * r
			dh = hx
			sw = self.img.size[0]
			sh = self.img.size[1]
		###
		return (int(dx), int(dy), int(dw), int(dh)), (int(sx), int(sy), int(sw), int(sh))

	def is_valid(self):
		return self._is_valid

	def make_linear_ramp(self, white):
		ramp = []
		###
		r, g, b = white
		###
		for i in range(255):
			ramp.extend((r*i/255, g*i/255, b*i/255))
		###
		return ramp

class CropImg(BaseImg):

	def __init__(self, res=None, key='', min_w=None, min_h=None, min_d=None):
		super(CropImg, self).__init__(min_w, min_h, min_d)
		###
		try:
			if key is None:
				self.img = Image.open(res)
			else:
				self.img = Image.open(res[key])
			###
			if self.img.mode not in self.m:
				self.img = self.img.convert(self.convert)
			###
			self._is_valid = self.valid()
		except IOError, e:
			self.error = e

	def getOriginSize(self):
		try:
			dpi = self.img.info['dpi']
		except:
			dpi = (72, 72)
		###
		return self.img.size[0], self.img.size[1], dpi

	def save(self, name=''):
		self.img.save(name, self.type_save, quality=self.quality)

	def resize(self, w=None, h=None):
		if w is not None:
			self.w = w
		###
		if w is not None:
			self.h = h
		###
		self.img = self.img.resize(self.getSize(float(self.img.size[0]), float(self.img.size[1])), Image.ANTIALIAS)

	def resize_only(self, w=None, h=None):
		if w is not None:
			self.w = w
		###
		if w is not None:
			self.h = h
		###
		new_size = self.getSizeCrop(self.w, self.h, self.w, self.h)
		###
		new = Image.new('RGB', (self.img.size[0], self.img.size[1]))
		new.paste(self.img)
		new = new.crop(new_size[1])
		###
		self.img = new.resize((new_size[0][2], new_size[0][3]), Image.ANTIALIAS)

	def thumb(self, name='', t_w=None, t_h=None):
		if t_w is not None:
			self.t_w = t_w
		###
		if t_h is not None:
			self.t_h = t_h
		###
		img = Image.new('RGB', (self.img.size[0], self.img.size[1]))
		###
		img.paste(self.img)
		###
		img.thumbnail((self.t_w, self.t_h), Image.ANTIALIAS)
		###
		img.save(name, self.type_save, quality=self.quality-30)

	def valid(self):
		is_valid = False
		###
		w, h, dpi = self.getOriginSize()
		###
		if ((w >= self.min_w) and (h >= self.min_h)):
			if ((dpi[0] >= self.min_d) and (dpi[1] >= self.min_d)):
				is_valid = True
			else:
				self.error = "Изображение низкого качества. Загрузите изображение больше чем %s dpi" % (self.min_d,)
		else:
			self.error = "Изображение должно быть больше чем %sx%s" % (self.min_w, self.min_h)
		###
		return is_valid

	def sepia(self):
		sepia = self.make_linear_ramp((255, 240, 192))
		###
		orig_mode = self.img.mode
		###
		if not orig_mode == 'L':
			self.img = self.img.convert('L')
		###
		self.img.putpalette(sepia)
		###
		if not orig_mode == 'L':
			self.img = self.img.convert(orig_mode)

	def BlackWhite(self):
		orig_mode = self.img.mode
		###
		if not orig_mode == 'L':
			self.img = self.img.convert('L')
		###
		self.img.convert('1')

class Img(object):

	w = 80
	h = 170

	def resize(self, img_files=None, key='file'):
		self.img = False
		###
		try:
			self.img = Image.open(img_files[key])
			###
			if self.img.mode not in self.m:
				self.img = img.convert('RGB')
			###
			self.img = self.img.resize(self.getSize(float(self.img.size[0]), float(self.img.size[1])), Image.ANTIALIAS)
		except IOError, e:
			self.error = e
		###
		return self.img

class CookieListBase(object):
	
	days = 14

	def __init__(self, cookie_key='nobody'):
		self.days_expire = self.days * 24 * 60 * 60
		###
		self.cookie_key = cookie_key

	def getExpires(self):
		return datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=self.days_expire), "%a, %d-%b-%Y %H:%M:%S GMT")

	def set_data(self, response=None, val=[]):
		response.set_cookie(self.cookie_key, pickle.dumps(val), max_age=self.days_expire, expires=self.getExpires())
		###
		return response

class CookieListFiles(CookieListBase):

	def __init__(self):
		super(CookieListFiles, self).__init__(cookie_key='nobody_data')

	def get_data(self, request):
		from collage.crop.settings import *
		###
		thumbs = []
		###
		if request.COOKIES.has_key(self.cookie_key):
			try:
				data = pickle.loads(request.COOKIES[self.cookie_key])
				###
				if not type(data).__name__ == 'list':
					data = []
				###
				for f in data:
					if os.path.isfile(''.join([FILES_DIR, DIR_NOBODY, f, '.', SAVE_IMG_EXT])):
						thumbs.append(f)
			except:
				pass
		###
		return thumbs
		
class CookieListOptions(CookieListBase):

	def __init__(self):
		super(CookieListOptions, self).__init__(cookie_key='nobody_data_opt')

	def get_data(self, request):
		from collage.crop.settings import *
		###
		opt = []
		###
		if request.COOKIES.has_key(self.cookie_key):
			try:
				data = pickle.loads(request.COOKIES[self.cookie_key])
				print data
				###
				if not type(data).__name__ == 'list':
					data = []
				###
				for f in data:
					if os.path.isfile(''.join([FILES_DIR, DIR_NOBODY, f['char_id'], '.', SAVE_IMG_EXT])):
						opt.append({
							'char_id':f['char_id'],
							'img_stretch':int(f['img_stretch']),
							'img_type':int(f['img_type']),
							'img_size':int(f['img_size']),
							'img_effect':int(f['img_effect']),
							'qty':int(f['qty']),
							'frame':int(f['frame']),
							'packaging':int(f['packaging']),
							'x1':int(f['x1']),
							'y1':int(f['y1']),
							'x2':int(f['x2']),
							'y2':int(f['y2']),
						})
			except:
				pass
		###
		return opt

class CookieMosaicOption(CookieListBase):

	def __init__(self):
		super(CookieMosaicOption, self).__init__(cookie_key='nobody_mosaic_opt')

	def isFile(self, f=''):
		from collage.mosaic.settings import *
		###
		if os.path.isfile(''.join([FILES_DIR, DIR_NOBODY, f, '.', SAVE_IMG_EXT])):
			return f
		else:
			return ''

	def setKeyData(self, item=None, key='', t='char'):
		val = ''
		###
		try:
			if t == 'char':
				val = item[key]
			if t == 'int':
				if not type(item[key]).__name__ == 'int':
					val = int(item[key])
				else:
					val = item[key]
		except:
			if t == 'char':
				val = ''
			if t == 'int':
				val = 0
		###
		return val

	def get_data(self, request):
		from collage.mosaic.settings import *
		###
		opt = []
		###
		if request.COOKIES.has_key(self.cookie_key):
			try:
				data = pickle.loads(request.COOKIES[self.cookie_key])
				###
				if not type(data).__name__ == 'list':
					data = []
				###
			except:
				pass
			###
			for item in data:
				row = {
					'opt_id':self.setKeyData(item=item, key='opt_id', t='int'),
					'ext':SAVE_IMG_EXT,
					'pth':''.join([MEDIA_URL, MEDIA_URL_FILES, DIR_NOBODY,]),
					'qty':self.setKeyData(item=item, key='qty', t='int'),
					'table_type':self.setKeyData(item=item, key='table_type', t='int'),
					'table_size':self.setKeyData(item=item, key='table_size', t='int'),
					'effect':self.setKeyData(item=item, key='effect', t='int'),
					'frame':self.setKeyData(item=item, key='frame', t='int'),
					'packaging':self.setKeyData(item=item, key='packaging', t='int'),
					'user_id':0,
					'f_0':self.isFile(self.setKeyData(item=item, key='f_0')),
					'f_1':self.isFile(self.setKeyData(item=item, key='f_1')),
					'f_2':self.isFile(self.setKeyData(item=item, key='f_2')),
					'f_3':self.isFile(self.setKeyData(item=item, key='f_3')),
					'f_4':self.isFile(self.setKeyData(item=item, key='f_4')),
					'f_5':self.isFile(self.setKeyData(item=item, key='f_5')),
					'f_6':self.isFile(self.setKeyData(item=item, key='f_6')),
					'f_7':self.isFile(self.setKeyData(item=item, key='f_7')),
					'f_8':self.isFile(self.setKeyData(item=item, key='f_8')),
				}
				###
				if ((row['table_type'] in (1, 2, 3,)) and (row['opt_id'] > 0) and (row['effect'] in (1, 2, 3,)) and (row['qty'] > 0)):
					opt.append(row)
		###
		return opt

class CookiePuzzleFiles(CookieListBase):

	def __init__(self):
		super(CookiePuzzleFiles, self).__init__(cookie_key='nobody_puzzle')

	def get_data(self, request):
		from collage.puzzle.settings import *
		###
		thumbs = []
		###
		if request.COOKIES.has_key(self.cookie_key):
			try:
				data = pickle.loads(request.COOKIES[self.cookie_key])
				###
				if not type(data).__name__ == 'list':
					data = []
				###
				for f in data:
					if os.path.isfile(''.join([FILES_DIR, DIR_NOBODY, f, '.', SAVE_IMG_EXT])):
						thumbs.append(f)
			except:
				pass
		###
		return thumbs

class CookiePuzzleOption(CookieListBase):

	def __init__(self):
		super(CookiePuzzleOption, self).__init__(cookie_key='nobody_puzzle_opt')

	def get_data(self, request):
		from collage.puzzle.settings import *
		###
		opt = []
		###
		if request.COOKIES.has_key(self.cookie_key):
			try:
				data = pickle.loads(request.COOKIES[self.cookie_key])
				print data
				###
				if not type(data).__name__ == 'list':
					data = []
				###
				for f in data:
					if os.path.isfile(''.join([FILES_DIR, DIR_NOBODY, f['char_id'], '.', SAVE_IMG_EXT])):
						opt.append({
							'char_id':f['char_id'],
							'img_stretch':int(f['img_stretch']),
							'img_type':int(f['img_type']),
							'img_size':int(f['img_size']),
							'img_effect':int(f['img_effect']),
							'qty':int(f['qty']),
							'frame':int(f['frame']),
							'packaging':int(f['packaging']),
						})
			except:
				pass
		###
		return opt
