# -*- coding: utf-8 -*-

from django.forms.widgets import RadioFieldRenderer, RadioSelect, RadioInput
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from collage.crop.models import CropPrice

class RowPrice(object):

	data = None

	def __init__(self, data):
		self.data = data

	def get(self, row_id):
		ret = ''
		###
		for p in self.data:
			if p.size_id == row_id:
				ret = p
				###
				break
		###
		return ret

RP = RowPrice(CropPrice.objects.all())

class RowRadioInput(RadioInput):

	def __unicode__(self):
		if 'id' in self.attrs:
			label_for = ' for="%s_%s"' % (self.attrs['id'], self.index)
		else:
			label_for = ''
		###
		choice_label = conditional_escape(force_unicode(self.choice_label))
		###
		return mark_safe(u'<label%s>%s %s - (%s)</label>' % (label_for, self.tag(), choice_label, RP.get(self.index)))

class ColumnRadioFieldRenderer(RadioFieldRenderer):

	rows_in_col = 6

	def __iter__(self):
		for i, choice in enumerate(self.choices):
			yield RowRadioInput(self.name, self.value, self.attrs.copy(), choice, i)

	def __getitem__(self, idx):
		choice = self.choices[idx]
		###
		return RowRadioInput(self.name, self.value, self.attrs.copy(), choice, idx)

	def render(self):
		item_all = 0
		###
		for w in self:
			item_all = item_all + 1
		###
		out = ''
		ul = u'<ul id="ul_size_%s" class="left" style="padding-right: 20px;">\n%s\n</ul>'
		ul_id = 0
		i = 1
		items = ''
		###
		for w in self:
			items = ''.join([items, u'<li>%s</li>' % force_unicode(w),])
			###
			if ((i == item_all) or (i == self.rows_in_col)):
				out = ''.join([out, ul % (ul_id, items),])
				###
				ul_id = ul_id + 1
				###
				items = ''
			###
			i = i + 1
		###
		return mark_safe(out)

class ColumnRadioSelect(RadioSelect):
	renderer = ColumnRadioFieldRenderer
