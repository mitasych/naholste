# -*- coding: utf-8 -*-
from django.forms.widgets import Widget, Select
from django.utils.safestring import mark_safe
from django.template import Context, loader
from itertools import chain
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode

from collage.common.settings import STATIC_URL, MEDIA_URL

class ChoiceSize(Widget):

	css_def = ''
	css_sel = ''
	f_name = ''
	curr_title = ''
	curr_price = 0.00
	curr_src = ''
	choices = ()
	data = ()
	width = 0
	height = 0
	after = []

	def __init__(self, attrs=None, choices=()):
		super(ChoiceSize, self).__init__(attrs)
		###
		self.data = self.choices = list(choices)

	def render(self, name='', value='', attrs=None, choices=()):
		self.after = []
		self.f_name = name
		self.css_sel = u'frame_item_select left'
		self.css_def = u'frame_item left'
		###
		if value is None or value == '':
			value = 0
		else:
			value = int(value)
		###
		options = self.render_options(self.data, [value])
		###
		final_attrs = self.build_attrs(attrs, name=name)
		###
		data = {
			'name':name,
			'options':options,
			'title':self.curr_title,
			'price':'%.2f' % self.curr_price,
			'src':self.curr_src,
			'value':value,
			'cssdef':self.css_def,
			'csssel':self.css_sel,
			'width':self.width,
			'height':self.height,
			'after':mark_safe(''.join(self.after))
		}
		###
		t = loader.get_template('puzzle_widget_choice_size.html')
		c = Context(data)
		###
		return t.render(c)

	def render_options(self, choices, selected_choices):
		options = []
		###
		for option in choices:
			options.append(self.render_option(option, selected_choices))
		###
		return options

	def render_option(self, option, selected_choices):
		if option.id in selected_choices:
			css = self.css_sel
			###
			self.curr_title = option.name
			self.curr_price = option.price
			self.height = option.height
			self.width = option.width
			self.curr_src = ''.join([MEDIA_URL, option.img.name])
		else:
			css = self.css_def
		###
		params = {
			'name':self.f_name,
			'value':escape(str(option.id)),
			'css':css,
			'src':''.join([MEDIA_URL, option.img.name]),
			'title':option.name,
			'price':'%.2f' % option.price,
			'width':option.width,
			'height':option.height,
		}
		###
		self.after.append(u"""
			o%(name)sData.items[%(value)s] = {
				'src':'%(src)s',
				'title':'%(title)s',
				'price':(%(price)s).toFixed(2),
				'width':%(width)s,
				'height':%(height)s
			};
		""" % params)
		###
		return u"""
			<a href="javascript: o%(name)sData.selectItem(%(value)s);">
				<div id="%(name)s_item_%(value)s" class="%(css)s">
					<img src="%(src)s" alt="" /><br />
					<span class="item_title">%(title)s</span><br />
					<span class="item_price">%(price)s тенге</span>
				</div>
			</a>
		""" % params
