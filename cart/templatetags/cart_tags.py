# -*- coding: utf-8 -*-
import datetime
from django import template

register = template.Library()

def show_block(opt):
	return {'opt': opt}

def show_block_mail(context, opt):
	request = context['request']
	###
	return {
		'opt': opt,
		'domain':request.CART.domain,
	}

register.inclusion_tag('templatetags/cart_element.html')(show_block)
register.inclusion_tag('templatetags/cart_element_mail.html', takes_context=True)(show_block_mail)
