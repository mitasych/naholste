# -*- coding: utf-8 -*-
from django.forms.widgets import Widget, Select
from django.utils.safestring import mark_safe
from django.template import Context, loader
from itertools import chain
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode
from collage.mosaic.models import MosaicSize

class ChoiceSize(Widget):

	f_name = ''
	curr_title = ''
	curr_price = 0.00
	choices = ()
	data = ()
	width = 0
	height = 0
	after = []
	rows_in_col = 4

	def __init__(self, attrs=None, choices=()):
		super(ChoiceSize, self).__init__(attrs)
		###
		self.data = self.choices = list(choices)

	def render(self, name='', value='', attrs=None, choices=()):
		self.data = self.choices = list(MosaicSize.objects.all())
		###
		self.after = []
		self.f_name = name
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
		item_all = len(options)
		###
		out = ''
		items = ''
		ul = u'<ul id="ul_size_%s" class="left" style="display: none; padding-right: 20px;">\n%s\n</ul>'
		ul_id = k = i = 1
		###
		for item in options:
			items = ''.join([items, item])
			###
			if ((k == item_all) or (i == self.rows_in_col)):
				out = ''.join([out, ul % (ul_id, items),])
				###
				items = ''
				###
				ul_id = ul_id + 1
				i = 0
			###
			i = i + 1
			k = k + 1
		###
		data = {
			'name':name,
			'out':out,
			'title':self.curr_title,
			'price':'%.2f' % self.curr_price,
			'value':value,
			'width':self.width,
			'height':self.height,
			'after':mark_safe(''.join(self.after))
		}
		###
		t = loader.get_template('mosaic_widget_choice_size.html')
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
		checked = ''
		###
		if option.id in selected_choices:
			self.curr_title = option.name
			self.curr_price = option.price
			self.height = option.height
			self.width = option.width
			checked = 'checked="checked"'
		###
		params = {
			'name':self.f_name,
			'value':escape(str(option.id)),
			'title':option.name,
			'price':'%.2f' % option.price,
			'checked':checked,
			'width':option.width,
			'height':option.height,
		}
		###
		self.after.append(u"""
			o%(name)sData.items[%(value)s] = {
				'title':'%(title)s',
				'price':(%(price)s).toFixed(2),
				'width':%(width)s,
				'height':%(height)s
			};
		""" % params)
		###
		return u"""
			<li>
				<label for="%(name)s_item_%(value)s">
					<input type="radio" value="%(value)s" id="id_%(name)s_%(value)s" name="%(name)s" %(checked)s onclick="o%(name)sData.selectItem(%(value)s);">
					%(title)s
				</label>
			</li>
		""" % params
