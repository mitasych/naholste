# -*- coding: utf-8 -*-
from settings import *
from django import forms
from django.forms.util import ErrorList
from collage.mosaic.models import MosaicOption, EFFECT_CHOISES, SIZE_CHOISES
from collage.crop.models import Frames, Packaging
from collage.common.widgets import FrameChoise

class MosaicOptionForm(forms.Form):

	opt_id = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=1, min_value=1)
	qty = forms.IntegerField(required=True, initial=1, min_value=1, max_value=1000)
	table_type = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=1, min_value=1, max_value=3)
	table_size = forms.IntegerField(required=True, initial=1, min_value=1, max_value=12)
	effect = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onclick':'oGlobalOption.effect_event(this)'}), required=True, initial=1, choices=EFFECT_CHOISES)
	frame = forms.ModelChoiceField(widget=FrameChoise(), queryset=Frames.objects.all(), initial=1)
	packaging = forms.ModelChoiceField(widget=FrameChoise(), queryset=Packaging.objects.all(), initial=1)
	f_0 = forms.CharField(widget=forms.HiddenInput(), required=False, initial='', max_length=32)
	f_1 = forms.CharField(widget=forms.HiddenInput(), required=False, initial='', max_length=32)
	f_2 = forms.CharField(widget=forms.HiddenInput(), required=False, initial='', max_length=32)
	f_3 = forms.CharField(widget=forms.HiddenInput(), required=False, initial='', max_length=32)
	f_4 = forms.CharField(widget=forms.HiddenInput(), required=False, initial='', max_length=32)
	f_5 = forms.CharField(widget=forms.HiddenInput(), required=False, initial='', max_length=32)
	f_6 = forms.CharField(widget=forms.HiddenInput(), required=False, initial='', max_length=32)
	f_7 = forms.CharField(widget=forms.HiddenInput(), required=False, initial='', max_length=32)
	f_8 = forms.CharField(widget=forms.HiddenInput(), required=False, initial='', max_length=32)

	def find(self, opts=[], opt_id=0):
		row = None
		###
		for i in opts:
			if i['opt_id'] == opt_id:
				row = i
				###
				break
		###
		return row

	class ObjRow:
		pass

	def getDefTableSize(self, table_type):
		table_size = 1
		###
		if table_type == 1:
			table_size = 1
		if table_type == 2:
			table_size = 5
		if table_type == 3:
			table_size = 9
		###
		return table_size

	def getDefObj(self, opt_id=0, table_type=1):
		obj = self.ObjRow
		###
		obj.opt_id = opt_id
		obj.qty = self['qty'].value()
		obj.table_type = table_type
		obj.table_size = self.getDefTableSize(table_type)
		obj.effect = self['effect'].value()
		obj.frame = 1
		obj.packaging = 1
		obj.ext = ''
		obj.pth = ''
		obj.f_0 = self['f_0'].value()
		obj.f_1 = self['f_1'].value()
		obj.f_2 = self['f_2'].value()
		obj.f_3 = self['f_3'].value()
		obj.f_4 = self['f_4'].value()
		obj.f_5 = self['f_5'].value()
		obj.f_6 = self['f_6'].value()
		obj.f_7 = self['f_7'].value()
		obj.f_8 = self['f_8'].value()
		###
		return obj

	def getDefRow(self, opt_id=0, table_type=1):
		return {
			'opt_id':opt_id,
			'qty':self['qty'].value(),
			'table_type':table_type,
			'table_size':self.getDefTableSize(table_type),
			'effect':self['effect'].value(),
			'frame':self['frame'].value(),
			'packaging':self['packaging'].value(),
			'ext':'',
			'pth':'',
			'f_0':self['f_0'].value(),
			'f_1':self['f_1'].value(),
			'f_2':self['f_2'].value(),
			'f_3':self['f_3'].value(),
			'f_4':self['f_4'].value(),
			'f_5':self['f_5'].value(),
			'f_6':self['f_6'].value(),
			'f_7':self['f_7'].value(),
			'f_8':self['f_8'].value(),
		}

	def getDataRow(self, obj):
		return {
			'opt_id':obj.opt_id,
			'qty':obj.qty,
			'table_type':obj.table_type,
			'table_size':obj.table_size,
			'effect':obj.effect,
			'frame':obj.frame,
			'packaging':obj.packaging,
			'ext':obj.ext,
			'pth':obj.pth,
			'f_0':obj.f_0,
			'f_1':obj.f_1,
			'f_2':obj.f_2,
			'f_3':obj.f_3,
			'f_4':obj.f_4,
			'f_5':obj.f_5,
			'f_6':obj.f_6,
			'f_7':obj.f_7,
			'f_8':obj.f_8,
		}

class MosaicUploadForm(forms.Form):

	opt_id = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=1, min_value=1)
	file = forms.ImageField(widget=forms.FileInput(attrs={}), label='Изображение')
	table_type = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=1, min_value=1, max_value=3)
	div_id = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=1, min_value=0, max_value=9)
	img_effect = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=1, min_value=1, max_value=3)

	class MosaicUploadFormList(ErrorList):
		def __unicode__(self):
			return self.as_divs()

		def as_divs(self):
			return ''

	def __init__(self, *args, **kwargs):
		super(MosaicUploadForm, self).__init__(*args, **kwargs)
		###
		self.error_class = self.MosaicUploadFormList
