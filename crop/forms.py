# -*- coding: utf-8 -*-
from django import forms
from collage.crop.settings import *
from collage.common.models import Stretch
from collage.crop.models import CropSize, Crop
from collage.crop.models import Frames, Packaging
from collage.common.widgets import SelectImage, RadioSelectNotNull
from collage.crop.widgets import ChoiceSize

SIZE_INIT = CropSize.objects.get(defsize=True)
STRETCH_INIT = Stretch.objects.get(defrow=True)

class CropForm(forms.ModelForm):

	to_cart = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=0, min_value=0, max_value=1)
	
	class Meta:
		model = Crop
		exclude = ('user', 'nouser', 'img', 'created')
		widgets = {
			'img_stretch':RadioSelectNotNull(attrs={'onclick':'oGlobalOption.stretch_event(this)'}),
			'img_type':RadioSelectNotNull(attrs={'onclick':'oGlobalOption.type_event(this)'}),
			'img_size':ChoiceSize(choices=CropSize.objects.all()),
			'img_effect':RadioSelectNotNull(attrs={'onclick':'oGlobalOption.effect_event(this)'}),
			'qty':forms.TextInput(attrs={'onchange':'oGlobalOption.qty_change()', 'onkeyup':'oGlobalOption.qty_event(event)'}),
			'frame':SelectImage(choices=Frames.objects.all()),
			'packaging':SelectImage(choices=Packaging.objects.all()),
			'x1':forms.HiddenInput(),
			'y1':forms.HiddenInput(),
			'x2':forms.HiddenInput(),
			'y2':forms.HiddenInput(),
		}

	def __init__(self, *args, **kwargs):
		super(CropForm, self).__init__(*args, **kwargs)

class UploadForm(forms.Form):
	
	file = forms.ImageField(widget=forms.FileInput(attrs={}), label='Изображение')

