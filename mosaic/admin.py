# -*- coding: utf-8 -*-

from django.contrib import admin
from collage.mosaic.models import MosaicPrice

class MosaicPriceAdmin(admin.ModelAdmin):

	fieldsets = [
		('Размер и цена', {'fields': ['size_id', 'price']}),
	]
	list_display = ['size_id', 'price']
	ordering = ('size_id',)

admin.site.register(MosaicPrice, MosaicPriceAdmin)
