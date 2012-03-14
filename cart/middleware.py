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
		###
		order = request.session.get('order', None)
		###
		if order is not None:
			try:
				order = int(order)
				###
				if order > 0:
					request.CART.set_order(order)
			except:
				pass
		###
		shiping = request.session.get('shiping', None)
		###
		if shiping is not None:
			try:
				shiping = int(shiping)
				###
				if shiping > 0:
					request.CART.set_shiping(shiping)
			except:
				pass

	def process_response(self, request, response):
		if hasattr(request, 'CART'):
			request.session['cart'] = request.CART.get()
		else:
			if hasattr(request, 'session'):
				request.session['cart'] = []
		###
		if hasattr(request, 'CART'):
			order = request.CART.get_order()
			###
			if order is not None:
				request.session['order'] = order.id
			###
			shiping = request.CART.get_shiping()
			###
			if shiping is not None:
				request.session['shiping'] = shiping.id
		else:
			if hasattr(request, 'session'):
				request.session['order'] = None
			###
			if hasattr(request, 'session'):
				request.session['shiping'] = None
		###
		return response
