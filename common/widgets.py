# -*- coding: utf-8 -*-
from django.forms.widgets import Widget, Textarea, Select, RadioSelect
from django.utils.safestring import mark_safe
from collage.settings import STATIC_URL
from itertools import chain
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode
from django.template import Context, loader

from settings import STATIC_URL, MEDIA_URL

class RadioSelectNotNull(RadioSelect):
	def get_renderer(self, name, value, attrs=None, choices=()):
		if value is None: value = ''
		###
		str_value = force_unicode(value)
		###
		final_attrs = self.build_attrs(attrs)
		choices = list(chain(self.choices, choices))
		###
		if choices[0][0] == '':
			choices.pop(0)
		###
		return self.renderer(name, str_value, final_attrs, choices)

class CKEditor(Textarea):

	class Media:
		js = ('/static/js/ckeditor/ckeditor.js',)

	def __init__(self, *args, **kwargs):
		super(CKEditor, self).__init__(*args, **kwargs)

	def render(self, name, value, attrs=None):
		rendered = super(CKEditor, self).render(name, value, attrs)
		###
		txt = mark_safe("""
			<script type="text/javascript"><!--
				jQuery(document).ready(
					function () {
						CKEDITOR.replace('%s', {height:"400", width:"687"});
					}
				);
			//--></script>
		""" % name)
		###
		return ' '.join([rendered, txt,])

class ImgName(object):
	name = u'no_choise_frame.jpg'

class NoneRow(object):
	id = 0
	name = u'Не выбрано'
	price = 0
	img = ImgName()

class SelectImage(Widget):

	css_def = ''
	css_sel = ''
	f_name = ''
	curr_title = ''
	curr_price = 0.00
	curr_src = ''
	choices = ()
	data = ()
	after = []

	def __init__(self, attrs=None, choices=()):
		super(SelectImage, self).__init__(attrs)
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
		if value <= 0: value = ''
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
			'after':mark_safe(''.join(self.after))
		}
		###
		t = loader.get_template('common_widget_choice.html')
		c = Context(data)
		###
		return t.render(c)

	def render_options(self, choices, selected_choices):
		options = []
		###
		options.append(self.render_option(NoneRow(), selected_choices))
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
		}
		###
		self.after.append(u"""
			o%(name)sData.items[%(value)s] = {
				'src':'%(src)s',
				'title':'%(title)s',
				'price':(%(price)s).toFixed(2)
			};
		""" % params)
		###
		return u"""
			<a href="javascript: o%(name)sData.selectItem(%(value)s);">
				<div id="%(name)s_item_%(value)s" class="%(css)s">
					<img src="%(src)s" alt="" /><br />
					<span class="item_title">%(title)s</span>
					<span class="item_price">%(price)s тенге</span>
				</div>
			</a>
		""" % params
