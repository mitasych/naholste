# -*- coding: utf-8 -*-

from django.contrib import admin

from gallery.models import Album, Images

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        (u'Описание', {'fields': ('name',  'img')}),
    )
    list_display = ('name', 'img')

class ImagesAdmin(admin.ModelAdmin):
    fieldsets = (
        (u'Описание', {'fields': ('album', 'name',  'img', )}),
    )
    list_display = ('preview_image_url', 'name', 'img', 'album')
    search_fields = ['name']
    list_filter = ['album']

admin.site.register(Album, AlbumAdmin)
admin.site.register(Images, ImagesAdmin)