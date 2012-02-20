# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from collage.puzzle.models import PuzzleSize

class PuzzleSizeForm(forms.ModelForm):
	class Meta:
		model = PuzzleSize

	def clean_price(self):
		price = float(self.cleaned_data['price'])
		###
		if price <= 0:
			raise forms.ValidationError(u'Цена должна быть больше нуля')
		else:
			return self.cleaned_data['price']

	def clean_width(self):
		s = int(self.cleaned_data['width'])
		###
		if s <= 0:
			raise forms.ValidationError(u'Ширина должна быть больше нуля')
		else:
			return self.cleaned_data['width']

	def clean_height(self):
		s = int(self.cleaned_data['height'])
		###
		if s <= 0:
			raise forms.ValidationError(u'Высота должна быть больше нуля')
		else:
			return self.cleaned_data['height']

class PuzzleSizeAdmin(admin.ModelAdmin):
	form = PuzzleSizeForm
	fieldsets = (
		(u'Описание', {'fields': ('name', 'price', 'img', 'width', 'height', 'defsize')}),
	)
	list_display = ('preview_image_url', 'name', 'price', 'img', 'width', 'height', 'defsize')

admin.site.register(PuzzleSize, PuzzleSizeAdmin)
