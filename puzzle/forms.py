# -*- coding: utf-8 -*-
from django import forms
from collage.puzzle.settings import *
from collage.common.models import Stretch
from collage.puzzle.models import PuzzleSize, Puzzle
from collage.puzzle.models import Frames, Packaging
from collage.puzzle.widgets import ChoiceSize
from collage.common.widgets import SelectImage, RadioSelectNotNull

SIZE_INIT = PuzzleSize.objects.get(defsize=True)
STRETCH_INIT = Stretch.objects.get(defrow=True)

class PuzzleForm(forms.ModelForm):

	to_cart = forms.IntegerField(widget=forms.HiddenInput(), required=True, initial=0, min_value=0, max_value=1)
	
	class Meta:
		model = Puzzle
		exclude = ('user', 'nouser', 'img', 'status', 'created')
		widgets = {
			'img_stretch':RadioSelectNotNull(attrs={'onclick':'oGlobalOption.stretch_event(this)'}),
			'img_size':ChoiceSize(choices=PuzzleSize.objects.all()),
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
		super(PuzzleForm, self).__init__(*args, **kwargs)

class UploadForm(forms.Form):
	
	file = forms.ImageField(widget=forms.FileInput(attrs={}), label='Изображение')
