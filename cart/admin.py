# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.db.models import Q
from collage.cart.models import Shiping, Currency, ShipingType, Countries, Cities

class CitiesForm(forms.ModelForm):
	
	class Meta:
		model = Cities

class CountriesForm(forms.ModelForm):
	
	class Meta:
		model = Countries

class ShipingTypeForm(forms.ModelForm):
	
	class Meta:
		model = ShipingType

class CurrencyForm(forms.ModelForm):
	
	class Meta:
		model = Currency

	def clean_factor(self):
		factor = float(self.cleaned_data['factor'])
		###
		if factor <= 0:
			raise forms.ValidationError(u'Коэффициент должн быть больше нуля')
		else:
			return factor

	def clean_code(self):
		code = self.cleaned_data['code']
		###
		q = self.instance.id is None and Q(code=code) or Q(~Q(id=self.instance.id), code=code)
		###
		if Currency.objects.filter(q).exists():
			raise forms.ValidationError(u'Код валюты не уникальный')
		else:
			return code

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

class CitiesAdmin(admin.ModelAdmin):
	
	form = CitiesForm
	fieldsets = (
		(u'Описание', {'fields': ('country', 'name',)}),
	)
	list_display = ('name', 'country',)
	ordering = ('country', 'name',)

class CountriesAdmin(admin.ModelAdmin):
	
	form = CountriesForm
	fieldsets = (
		(u'Описание', {'fields': ('name',)}),
	)
	list_display = ('name',)
	ordering = ('name',)

class ShipingTypeAdmin(admin.ModelAdmin):
	
	form = ShipingTypeForm
	fieldsets = (
		(u'Описание', {'fields': ('name',)}),
	)
	list_display = ('name',)

class CurrencyAdmin(admin.ModelAdmin):
	
	form = CurrencyForm
	fieldsets = (
		(u'Описание', {'fields': ('name', 'code', 'factor')}),
	)
	list_display = ('name', 'code', 'factor')

class ShipingAdmin(admin.ModelAdmin):
	
	form = ShipingForm
	fieldsets = (
		(u'Описание', {'fields': ('shiping_type', 'country', 'city', 'price',)}),
	)
	list_display = ('shiping_type', 'country', 'city', 'price',)
	ordering = ['country', 'city']

admin.site.register(Cities, CitiesAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(ShipingType, ShipingTypeAdmin)
admin.site.register(Shiping, ShipingAdmin)
admin.site.register(Currency, CurrencyAdmin)
