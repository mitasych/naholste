# -*- coding: utf-8 -*-
from settings import *
from django import forms
from collage.crop.models import Frames, Packaging
from collage.common.widgets import FrameChoise
from collage.puzzle.widgets import FrameChoisePrice
from collage.puzzle.models import STRETCH_CHOISES, TYPE_CHOISES, SIZE_CHOISES, EFFECT_CHOISES

class OptionForm(forms.Form):

	img_stretch = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onclick':'oGlobalOption.stretch_event(this)'}), required=True, initial=1, choices=STRETCH_CHOISES)
	img_type = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onclick':'oGlobalOption.type_event(this)'}), required=True, initial=1, choices=TYPE_CHOISES)
	img_size = forms.ChoiceField(widget=FrameChoisePrice(attrs={'onclick':'oGlobalOption.size_event(this)'}), required=True, initial=1, choices=SIZE_CHOISES)
	img_effect = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onclick':'oGlobalOption.effect_event(this)'}), required=True, initial=1, choices=EFFECT_CHOISES)
	qty = forms.IntegerField(widget=forms.TextInput(attrs={'onchange':'oGlobalOption.qty_change()', 'onkeyup':'oGlobalOption.qty_event(event)'}), required=True, initial=1, min_value=1, max_value=1000)
	frame = forms.ModelChoiceField(widget=FrameChoise(), queryset=Frames.objects.all(), initial=1)
	packaging = forms.ModelChoiceField(widget=FrameChoise(), queryset=Packaging.objects.all(), initial=1)
	to_cart = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=0, min_value=0, max_value=1)

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
		obj.to_cart = 0
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
			'to_cart':0,
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
			'to_cart':0,
		}

class UploadForm(forms.Form):
	
	file = forms.ImageField(widget=forms.FileInput(attrs={}), label='Изображение')

