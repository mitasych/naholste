# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from collage.mosaic.models import MosaicSize

class MosaicSizeForm(forms.ModelForm):
	class Meta:
		model = MosaicSize

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

class MosaicSizeAdmin(admin.ModelAdmin):
	form = MosaicSizeForm
	fieldsets = (
		(u'Описание', {'fields': ('name', 'price', 'width', 'height', 'defsize')}),
	)
	list_display = ('name', 'price', 'width', 'height', 'defsize')

admin.site.register(MosaicSize, MosaicSizeAdmin)
