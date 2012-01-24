# -*- coding: utf-8 -*-

from django.contrib import admin
from collage.puzzle.models import PuzzlePrice

class PuzzlePriceAdmin(admin.ModelAdmin):

	fieldsets = [
		('Размер и цена', {'fields': ['size_id', 'price']}),
	]
	list_display = ['size_id', 'price']
	ordering = ('size_id',)

admin.site.register(PuzzlePrice, PuzzlePriceAdmin)
