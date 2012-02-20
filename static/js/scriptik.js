function ThisFormSubmit(thisformid) {
	thisform = document.getElementById(thisformid);
	thisform.submit();
}

function getHtmlDiv() {
	var out = '';
	///
	out = out + '<div class="container_24">';
	out = out + '  <div class="wrapper">';
	out = out + '    <a href="javascript: hideMessage();" class="right" style="position: relative; top:2px; margin-right:12px;">';
	out = out + '      <img src="/static/images/close.png" alt="" class="close" />';
	out = out + '    </a>';
	out = out + '    <center>';
	out = out + '      <div class=":class">';
	out = out + '        :text';
	out = out + '      </div>';
	out = out + '    </center>';
	out = out + '  </div>';
	out = out + '</div>';
	///
	return out;
}

function hideMessage() {
	jQuery('#messages').hide();
}

function setUpload() {
	var formname = document.getElementById('upload_form');
	///
	var div_mess = getHtmlDiv();
	///
	jQuery("#upload_form").hide();
	jQuery("#progress").show();
	///
	if (jQuery("#id_img").val() != "") {
		jQuery.ajaxUpload({
			url:'/crop/uploadfile/',
			secureuri:false,
			uploadform: formname,
			dataType: 'json',
			fileUpload:true,
			success: function (data, status) {
				if (data.error == 0) {
					jQuery("#messages").html(div_mess.replace(':class', 'success').replace(':text', data.message));
					jQuery("#messages").show();
					///
					document.location = '/crop/option?id='+data.id;
				}
				else {
					jQuery("#messages").html(div_mess.replace(':class', 'error').replace(':text', data.message));
					jQuery("#messages").show();
				}
				///
				jQuery("#progress").hide();
				jQuery("#upload_form").show();
			},
			error: function (data, status, e, aa) {
				jQuery("#messages").html(div_mess.replace(':class', 'error').replace(':text', e));
				jQuery("#messages").show();
				///
				jQuery("#progress").hide();
				jQuery("#upload_form").show();
			}
		});
	}
	else {
		jQuery("#upload_form").show();
		///
		jQuery("#messages").html(div_mess.replace(':class', 'error').replace(':text', 'Выберите изображение'));
		jQuery("#messages").show();
	}
}

function delImage(set_url, key) {
	jQuery.ajax({
		type: 'get',
		url: set_url,
		data: '',
		dataType: 'json',
		success: function(data, status) {
			if (data.error == 0) {
				jQuery('#'+key).hide();
			}
		},
		error: function(data, status, e) {
			alert(e);
		}
	});
}

function effectImage(set_url) {
	jQuery.ajax({
		type: 'get',
		url: set_url,
		data: '',
		dataType: 'json',
		success: function(data, status) {
			if (data.error == 0) {
				jQuery('#img_thumb_prev').attr({'src':data.file});
			}
		},
		error: function(data, status, e) {
			alert(e);
		}
	});
}

function setMosaicUpload(opt_id, div_id) {
	var formname = document.getElementById('upload_form_'+div_id);
	///
	var div_mess = getHtmlDiv();
	///
	jQuery("#upload_form_"+div_id).hide();
	jQuery("#progress_"+div_id).show();
	///
	jQuery.ajaxUpload({
		url:'/mosaic/uploadfile/?id='+opt_id,
		secureuri:false,
		uploadform: formname,
		dataType: 'json',
		fileUpload:true,
		success: function (data, status) {
			if (data.error == 0) {
				htm = '<img id="img_thumb_' + div_id + '" src="' + data.url + '" alt="" />'
				///
				jQuery("#messages").html(div_mess.replace(':class', 'success').replace(':text', data.message));
				jQuery("#messages").show();
				///
				jQuery("#td_"+div_id).html(htm);
			}
			else {
				jQuery("#messages").html(div_mess.replace(':class', 'error').replace(':text', data.message));
				jQuery("#messages").show();
			}
			///
			jQuery("#progress_"+div_id).hide();
			jQuery("#upload_form_"+div_id).show();
		},
		error: function (data, status, e, aa) {
			jQuery("#messages").html(div_mess.replace(':class', 'error').replace(':text', e));
			jQuery("#messages").show();
			///
			jQuery("#progress_"+div_id).hide();
			jQuery("#upload_form_"+div_id).show();
		}
	});
}

function effectMosaicImage(set_url) {
	jQuery.ajax({
		type: 'get',
		url: set_url,
		data: '',
		dataType: 'json',
		success: function(data, status) {
			if (data.error == 0) {
				for (var i = 0; i < 9; i++) {
					jQuery('#img_thumb_'+i).attr({'src':data['f_'+i]});
				}
			}
		},
		error: function(data, status, e) {
			alert(e);
		}
	});
}

function setPuzzleUpload() {
	var formname = document.getElementById('upload_form');
	///
	var div_mess = getHtmlDiv();
	///
	jQuery("#upload_form").hide();
	jQuery("#progress").show();
	///
	if (jQuery("#id_img").val() != "") {
		jQuery.ajaxUpload({
			url:'/puzzle/uploadfile/',
			secureuri:false,
			uploadform: formname,
			dataType: 'json',
			fileUpload:true,
			success: function (data, status) {
				if (data.error == 0) {
					jQuery("#messages").html(div_mess.replace(':class', 'success').replace(':text', data.message));
					jQuery("#messages").show();
					///
					document.location = '/puzzle/option?id='+data.id;
				}
				else {
					jQuery("#messages").html(div_mess.replace(':class', 'error').replace(':text', data.message));
					jQuery("#messages").show();
				}
				///
				jQuery("#progress").hide();
				jQuery("#upload_form").show();
			},
			error: function (data, status, e, aa) {
				jQuery("#messages").html(div_mess.replace(':class', 'error').replace(':text', e));
				jQuery("#messages").show();
				///
				jQuery("#progress").hide();
				jQuery("#upload_form").show();
			}
		});
	}
	else {
		jQuery("#upload_form").show();
		///
		jQuery("#messages").html(div_mess.replace(':class', 'error').replace(':text', 'Выберите изображение'));
		jQuery("#messages").show();
	}
}

function setValCart(v) {
	$('#id_to_cart').val(v);
}

function Sizer() {
	this.jcrop_api = false;
	///
	this.w = 0;
	this.h = 0;
	///
	this.x1 = 0;
	this.y1 = 0;
	this.x2 = 0;
	this.y2 = 0;
	///
	this.img_stretch = 0;
	///
	this.css_v = {'background':'#ffffff','filter':'alpha(opacity=40)','opacity':'0.4','width':'16px !important'};
	this.css_h = {'background':'#ffffff','filter':'alpha(opacity=40)','opacity':'0.4','height':'16px !important'};
	this.css_tdv = {'background':'white url(/static/css/jcrop/Jcrop.gif) top left repeat','width':'1px !important'};
	this.css_tdh = {'background':'white url(/static/css/jcrop/Jcrop.gif) top left repeat','height':'1px !important'};
	this.css_bdv = {'background':'white url(/static/css/jcrop/Jcrop.gif) top left repeat','width':'1px !important'};
	this.css_bdh = {'background':'white url(/static/css/jcrop/Jcrop.gif) top left repeat','height':'1px !important'};
	///
	this.setStretch = function() {
		var css_v = this.css_v;
		var css_h = this.css_h;
		///
		var css_tdh = this.css_tdh;
		var css_bdh = this.css_bdh;
		var css_bdv = this.css_tdv;
		var css_tdv = this.css_bdv;
		///
		if (this.img_stretch == 2) {
			$('.jcrop-hline').css(css_h);
			$('.jcrop-hline[class=bottom]').css(css_h);
			$('.jcrop-vline').css(css_v);
			$('.jcrop-vline[class=right]').css(css_v);
		}
		else {
			$('.jcrop-hline').css(css_tdh);
			$('.jcrop-hline[class=bottom]').css(css_bdh);
			$('.jcrop-vline').css(css_tdv);
			$('.jcrop-vline[class=right]').css(css_bdv);
		}
	};
	///
	this.setCoord = function(x1, y1, x2, y2) {
		this.x1 = x1;
		this.y1 = y1;
		this.x2 = x2;
		this.y2 = y2;
		///
		$('#id_x1').val(Math.floor(x1));
		$('#id_y1').val(Math.floor(y1));
		$('#id_x2').val(Math.floor(x2));
		$('#id_y2').val(Math.floor(y2));
		///
		this.jcrop_api.animateTo([x1, y1, x2, y2]);
		///
		this.jcrop_api.setOptions({
			minSize: [(x2 - x1), (y2 - y1)],
			maxSize: [(x2 - x1), (y2 - y1)]
		});
	};
	///
	this.getProp = function() {};
	///
	this.wCreateCanvas = function() {
		var pr = this.getProp();
		///
		var w = this.w - 1;
		var h = this.h - 1;
		///
		var one_w = w / pr[0];
		var one_h = one_w * pr[1];
		///
		if (one_h <= h) {
			h = one_h;
		}
		else {
			while (w > 0) {
				w = w - 1;
				///
				one_w = w / pr[0];
				one_h = one_w * pr[1];
				///
				if (one_h <= h) {
					h = one_h;
					///
					break;
				}
			}
		}
		///
		var to_y1 = (this.h - h) / 2;
		///
		var to_x1 = (this.w - w) / 2;
		///
		if (to_x1 < 0) {
			to_x1 = 0;
		}
		///
		var to_x2 = to_x1 + w;
		///
		var to_y2 = to_y1 + h;
		///
		this.setCoord(to_x1, to_y1, to_x2, to_y2);
	};
	///
	this.hCreateCanvas = function() {
		var pr = this.getProp();
		///
		var w = this.w;
		var h = this.h;
		///
		var one_h = h / pr[0];
		var one_w = one_h * pr[1];
		///
		if (one_w <= w) {
			w = one_w;
		}
		else {
			while (h > 0) {
				h = h - 1;
				///
				one_h = h / pr[0];
				one_w = one_h * pr[1];
				///
				if (one_w <= w) {
					w = one_w;
					///
					break;
				}
			}
		}
		///
		var to_x1 = (this.w - w) / 2;
		///
		var to_y1 = (this.h - h) / 2;
		///
		if (to_y1 < 0) {
			to_y1 = 0;
		}
		///
		var to_x2 = to_x1 + w;
		///
		var to_y2 = to_y1 + h;
		///
		this.setCoord(to_x1, to_y1, to_x2, to_y2);
	};
	///
	this.ul_id = "#price_info";
	this.ul = "<ul>:li</ul>";
	this.li = '<li><span class="left">:name</span><span class="right">:price тенге</span></li>\n';
	///
	this.show_price = function(data) {
		var li = '';
		var price = 0.00;
		///
		if (data.length > 0) {
			for (var key in data) {
				price = price + data[key].price;
				///
				li = li + this.li.replace(':name', data[key].name).replace(':price', data[key].price.toFixed(2));
			}
			///
			price = '<div class="clear"></div><hr /><p class="right">' + price.toFixed(2) + ' тенге</p>'
			///
			$(this.ul_id).html(this.ul.replace(':li', li) + price)
		}
	};
}
