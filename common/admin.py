# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from collage.common.models import Frames, Packaging, Stretch

class FramesForm(forms.ModelForm):
	class Meta:
		model = Frames

	def clean_price(self):
		price = float(self.cleaned_data['price'])
		###
		if price <= 0:
			raise forms.ValidationError(u'Цена должна быть больше нуля')
		else:
			return self.cleaned_data['price']

class PackagingForm(forms.ModelForm):
	class Meta:
		model = Packaging

	def clean_price(self):
		price = float(self.cleaned_data['price'])
		###
		if price <= 0:
			raise forms.ValidationError(u'Цена должна быть больше нуля')
		else:
			return self.cleaned_data['price']

class StretchForm(forms.ModelForm):
	class Meta:
		model = Stretch

	def clean_koef(self):
		koef = float(self.cleaned_data['koef'])
		###
		if koef <= 0:
			raise forms.ValidationError(u'Коэфициент должен быть больше нуля')
		else:
			return self.cleaned_data['koef']

class FramesAdmin(admin.ModelAdmin):
	form = FramesForm
	fieldsets = (
		(u'Описание', {'fields': ('name', 'price', 'img')}),
	)
	list_display = ('preview_image_url', 'name', 'price', 'img')

class PackagingAdmin(admin.ModelAdmin):
	form = PackagingForm
	fieldsets = (
		(u'Описание', {'fields': ('name', 'price', 'img')}),
	)
	list_display = ('preview_image_url', 'name', 'price', 'img')

class StretchAdmin(admin.ModelAdmin):
	form = StretchForm
	fieldsets = (
		(u'Описание', {'fields': ('name', 'koef', 'descr', 'defrow')}),
	)
	list_display = ('name', 'koef', 'descr', 'defrow')

admin.site.register(Frames, FramesAdmin)
admin.site.register(Packaging, PackagingAdmin)
admin.site.register(Stretch, StretchAdmin)
