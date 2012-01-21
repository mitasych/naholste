# -*- coding: utf-8 -*-

from django.forms.widgets import RadioFieldRenderer, RadioSelect
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode

class ColumnRadioFieldRenderer(RadioFieldRenderer):

	rows_in_col = 6

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
