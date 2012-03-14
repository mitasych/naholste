# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from collage.cart.models import Shiping

class ShipingForm(forms.ModelForm):
	class Meta:
		model = Shiping

	def clean_price(self):
		price = float(self.cleaned_data['price'])
		###
		if price <= 0:
			raise forms.ValidationError(u'Цена должна быть больше нуля')
		else:
			return self.cleaned_data['price']

class ShipingAdmin(admin.ModelAdmin):
	form = ShipingForm
	fieldsets = (
		(u'Описание', {'fields': ('name', 'price')}),
	)
	list_display = ('name', 'price')

admin.site.register(Shiping, ShipingAdmin)
