# -*- coding: utf-8 -*-

from django.contrib import admin
from collage.crop.models import CropPrice

class CropPriceAdmin(admin.ModelAdmin):

	fieldsets = [
		('Размер и цена', {'fields': ['size_id', 'price']}),
	]
	list_display = ['size_id', 'price']
	ordering = ('size_id',)

admin.site.register(CropPrice, CropPriceAdmin)
