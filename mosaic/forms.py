# -*- coding: utf-8 -*-
from django import forms
from django.forms.util import ErrorList

from collage.mosaic.settings import *
from collage.common.models import Frames, Packaging
from collage.mosaic.models import MosaicSize, Mosaic, TYPE_CHOISES
from collage.common.widgets import SelectImage, RadioSelectNotNull
from collage.mosaic.widgets import ChoiceSize

SIZE_INIT = MosaicSize.objects.get(defsize=True)

class MosaicForm(forms.ModelForm):

	to_cart = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=0, min_value=0, max_value=1)
	
	class Meta:
		model = Mosaic
		exclude = ('user', 'nouser', 'table_type', 'f_0', 'f_1', 'f_2', 'f_3', 'f_4', 'f_5', 'f_6', 'f_7', 'f_8')
		widgets = {
			'img_size':ChoiceSize(choices=MosaicSize.objects.all()),
			'img_effect':RadioSelectNotNull(attrs={'onclick':'oGlobalOption.effect_event(this)'}),
			'qty':forms.TextInput(attrs={'onchange':'oGlobalOption.qty_change()', 'onkeyup':'oGlobalOption.qty_event(event)'}),
			'frame':SelectImage(choices=Frames.objects.all()),
			'packaging':SelectImage(choices=Packaging.objects.all()),
		}

	def __init__(self, *args, **kwargs):
		super(MosaicForm, self).__init__(*args, **kwargs)

class UploadForm(forms.Form):

	file = forms.ImageField(widget=forms.FileInput(attrs={}), label='Изображение')
	div_id = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=1, min_value=0, max_value=9)
	effect = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=1, min_value=1, max_value=3)

	class ErrorUploadFormList(ErrorList):
		def __unicode__(self):
			return self.as_divs()

		def as_divs(self):
			return ''

	def __init__(self, *args, **kwargs):
		super(UploadForm, self).__init__(*args, **kwargs)
		###
		self.error_class = self.ErrorUploadFormList

class CreateForm(forms.Form):

	table_type = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=1, min_value=1, max_value=3)
