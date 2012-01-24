# -*- coding: utf-8 -*-
from django.forms.widgets import Textarea, Select
from django.utils.safestring import mark_safe
from collage.settings import STATIC_URL
from itertools import chain
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode
from collage.common.widgets import FrameChoise
from collage.puzzle.models import PuzzlePrice

class FrameChoisePrice(FrameChoise):

	def __init__(self, *args, **kwargs):
		super(FrameChoisePrice, self).__init__(*args, **kwargs)
		###
		self.price = PuzzlePrice.objects.all()

	def getPrice(self, val):
		ret = ''
		###
		for p in self.price:
			if p.size_id == val:
				ret = p.__unicode__()
				###
				break
		###
		return ret

	def render(self, name, value, attrs=None, choices=()):
		self.f_name = name
		self.css_sel = u'frame_item_select left'
		self.css_def = u'frame_item left'
		###
		self.pth = ''.join([STATIC_URL, 'images/', self.f_name, '/', '%s.jpg'])
		###
		if value is None:
			value = ''
		###
		options = self.render_options(choices, [value])
		###
		src = self.pth % (self.curr_name,)
		###
		final_attrs = self.build_attrs(attrs, name=name)
		###
		output = """
		<script type="text/javascript">
			function %(name)sData() {
				this.items = [];
				///
				this.showBlock = function() {
					$('#view_%(name)s').toggle();
				};
				///
				this.selectItem = function(item) {
					if (item > 0) {
						$('#img_name_%(name)s').html(this.items[item]['cod'] + "<br /><small>(" + this.items[item]['price'] + ")</small>");
						///
						$('#img_%(name)s').attr({'src':this.items[item]['src']});
						///
						for (var i in this.items) {
							$('#%(name)s_item_'+i).attr({'class':'%(cssdef)s'});
						}
						///
						$('#%(name)s_item_'+item).attr({'class':'%(csssel)s'});
						///
						$('#id_%(name)s').val(item);
						///
						$('#view_%(name)s').hide();
					}
				};
			}
			///
			o%(name)sData = new %(name)sData()
		</script>
		<div class="frame_parent">
			<div class="frame_choise">
				<a href="javascript: o%(name)sData.showBlock();">
					<div class="frame_click right"></div>
					<img id="img_%(name)s" src="%(src)s" /><br />
				</a>
				<center>
					<span id="img_name_%(name)s">%(cod)s<br /><small>%(price)s</small></span>
				</center>
			</div>
			<div class="frame_view" id="view_%(name)s">
				%(options)s
			</div>
			<input type="hidden" id="id_%(name)s" name="%(name)s" value="%(value)s" />
		</div>
		""" % {
			'name':name,
			'src':src,
			'options':options,
			'cod':self.curr_label,
			'value':value,
			'cssdef':self.css_def,
			'csssel':self.css_sel,
			'price':self.getPrice(value),
		}
		###
		return mark_safe(output)

	def render_option(self, selected_choices, option_value, option_label):
		option_value = int(force_unicode(option_value))
		option_label = conditional_escape(force_unicode(option_label))
		###
		if option_value in selected_choices:
			css = self.css_sel
			###
			if option_value == 1:
				self.curr_name = 'no_choise_frame'
				self.curr_label = u'нет'
			else:
				self.curr_label = self.curr_name = option_label
		else:
			css = self.css_def
		###
		if option_value == 1:
			pth = self.pth % ('no_choise_frame',)
		else:
			pth = self.pth % (option_label,)
		###
		return """
			<script type="text/javascript">
				o%(name)sData.items[%(value)s] = {'src':'%(src)s', 'cod':'%(label)s', 'price':'%(price)s'};
			</script>
			<a href="javascript: o%(name)sData.selectItem(%(value)s);">
				<div id="%(name)s_item_%(value)s" class="%(css)s">
					<img src="%(src)s" alt="" /><br />
					<span>%(label)s</span><br />
					<small>%(price)s</small>
				</div>
			</a>
		""" % {
			'name':self.f_name,
			'value':escape(option_value),
			'css':css,
			'src':pth,
			'label':option_label,
			'price':self.getPrice(option_value),
		}
