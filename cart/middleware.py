# -*- coding: utf-8 -*-

from collage.cart.cart import Cart

class CartMiddleware(object):

	def process_request(self, request):
		cart = request.session.get('cart', [])
		###
		if not type(cart).__name__ == 'list':
			cart = []
		###
		request.session['cart'] = cart
		###
		request.CART = Cart(cart)

	def process_response(self, request, response):
		if hasattr(request, 'CART'):
			request.session['cart'] = request.CART.get()
		else:
			if hasattr(request, 'session'):
				request.session['cart'] = []
		###
		return response
