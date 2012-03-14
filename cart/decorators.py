# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def choice_shiping():
	def decorator(func):
		def wrapper(request, *args, **kwargs):
			shiping = request.CART.get_shiping()
			print shiping
			###
			if shiping is None:
				return HttpResponseRedirect(reverse('cart.views.shiping'))
			else:
				return func(request, *args, **kwargs)
		###
		return wrapper
	###
	return decorator
