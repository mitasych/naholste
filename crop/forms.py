# -*- coding: utf-8 -*-
from settings import *
from django import forms
from collage.crop.models import Frames, Packaging
from collage.common.widgets import FrameChoise

STRETCH_CHOISES = (
	(1, u'Стандартная',),
	(2, u'Галерейная',),
	(3, u'Холст',),
)

TYPE_CHOISES = (
	(1, u'Альбомная',),
	(2, u'Книжная',),
)

SIZE_CHOISES = (
	(1, u'30x20 см',),
	(2, u'40x30 см',),
	(3, u'50x40 см',),
	(4, u'60x40 см',),
	(5, u'70x50 см',),
	(6, u'90x60 см',),
)

EFFECT_CHOISES = (
	(1, u'Нет',),
	(2, u'Черно-белое',),
	(3, u'Сепия',),
)

class OptionForm(forms.Form):

	img_stretch = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onclick':'oGlobalOption.stretch_event(this)'}), required=True, initial=1, choices=STRETCH_CHOISES)
	img_type = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onclick':'oGlobalOption.type_event(this)'}), required=True, initial=1, choices=TYPE_CHOISES)
	img_size = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onclick':'oGlobalOption.size_event(this)'}), required=True, initial=6, choices=SIZE_CHOISES)
	img_effect = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onclick':'oGlobalOption.effect_event(this)'}), required=True, initial=1, choices=EFFECT_CHOISES)
	qty = forms.IntegerField(widget=forms.TextInput(attrs={'onchange':'oGlobalOption.qty_change()', 'onkeyup':'oGlobalOption.qty_event(event)'}), required=True, initial=1, min_value=1, max_value=1000)
	frame = forms.ModelChoiceField(widget=FrameChoise(), queryset=Frames.objects.all(), initial=1)
	packaging = forms.ModelChoiceField(widget=FrameChoise(), queryset=Packaging.objects.all(), initial=1)
	x1 = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=0)
	y1 = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=0)
	x2 = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=0)
	y2 = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=0)

	def getStretch(self, val_id=0): return self.getVal(val_id, STRETCH_CHOISES)
	def getType(self, val_id=0): return self.getVal(val_id, TYPE_CHOISES)
	def getSize(self, val_id=0): return self.getVal(val_id, SIZE_CHOISES)
	def getEffect(self, val_id=0): return self.getVal(val_id, EFFECT_CHOISES)

	def getVal(self, val_id=0, data=()):
		ret = ''
		###
		if not type(val_id).__name__ == 'int':
			try:
				val_id = int(val_id)
			except:
				val_id = 0
		###
		for i in data:
			if i[0] == val_id:
				ret = i[1]
				###
				break
		###
		return ret

	def getStretchList(self): return self.getList(STRETCH_CHOISES)
	def getTypeList(self): return self.getList(TYPE_CHOISES)
	def getSizeList(self): return self.getList(SIZE_CHOISES)
	def getEffectList(self): return self.getList(EFFECT_CHOISES)

	def getList(self, data=()):
		ret = []
		###
		for i in data:
			ret.append({'id':i[0], 'name':i[1]})
		###
		return ret

	class ObjRow:
		pass

	def getDefObj(self, f=''):
		obj = self.ObjRow
		###
		obj.img_stretch = self['img_stretch'].value()
		obj.img_type = self['img_type'].value()
		obj.img_size = self['img_size'].value()
		obj.img_effect = self['img_effect'].value()
		obj.qty = self['qty'].value()
		obj.frame = Frames.objects.get(pk=1)
		obj.packaging = Packaging.objects.get(pk=1)
		obj.x1 = self['x1'].value()
		obj.y1 = self['y1'].value()
		obj.x2 = self['x2'].value()
		obj.y2 = self['y2'].value()
		###
		return obj

	def getDefRow(self, f=''):
		return {
			'char_id':f,
			'img_stretch':self['img_stretch'].value(),
			'img_type':self['img_type'].value(),
			'img_size':self['img_size'].value(),
			'img_effect':self['img_effect'].value(),
			'qty':self['qty'].value(),
			'frame':self['frame'].value(),
			'packaging':self['packaging'].value(),
			'x1':self['x1'].value(),
			'y1':self['y1'].value(),
			'x2':self['x2'].value(),
			'y2':self['y2'].value(),
		}

	def getDataRow(self, obj):
		return {
			'img_stretch':obj.img_stretch,
			'img_type':obj.img_type,
			'img_size':obj.img_size,
			'img_effect':obj.img_effect,
			'qty':obj.qty,
			'frame':obj.frame,
			'packaging':obj.packaging,
			'x1':obj.x1,
			'y1':obj.y1,
			'x2':obj.x2,
			'y2':obj.y2,
		}

class UploadForm(forms.Form):
	
	file = forms.ImageField(widget=forms.FileInput(attrs={}), label='Изображение')

