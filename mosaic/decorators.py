# -*- coding: utf-8 -*-
from collage.mosaic.models import Mosaic

def reload():
	def decorator(func):
		def wrapper(request, *args, **kwargs):
			user = request.user
			###
			if (user.is_authenticated() and user.is_active):
				nouser = request.NOUSER.get()
				###
				p = Mosaic.objects.filter(user=None, nouser=nouser)
				###
				if p.exists():
					p.update(user=user, nouser='')
			###
			return func(request, *args, **kwargs)
		###
		return wrapper
	###
	return decorator
