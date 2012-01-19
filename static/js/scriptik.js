function hideMessage() {
	jQuery('#messages').hide();
}

function setUpload() {
	formname = document.getElementById('upload_form');
	///
	jQuery("#error_img").hide();
	jQuery("#success_img").hide();
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
					jQuery("#success_img").html(data.message);
					jQuery("#success_img").show();
					///
					document.location = '/crop/option/'+data.file+'/';
				}
				else {
					jQuery("#error_img").html(data.message);
					jQuery("#error_img").show();
				}
				///
				jQuery("#progress").hide();
				jQuery("#upload_form").show();
			},
			error: function (data, status, e, aa) {
				jQuery("#error_img").html(e);
				jQuery("#error_img").show();
				jQuery("#progress").hide();
				jQuery("#upload_form").show();
			}
		});
	}
	else {
		jQuery("#upload_form").show();
		jQuery("#error_img").html('Выберите изображение');
		jQuery("#error_img").show();
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

function setMosaicUpload(div_id) {
	formname = document.getElementById('upload_form_'+div_id);
	///
	jQuery("#error_img_"+div_id).hide();
	jQuery("#success_img_"+div_id).hide();
	jQuery("#upload_form_"+div_id).hide();
	jQuery("#progress_"+div_id).show();
	///
	jQuery.ajaxUpload({
		url:'/mosaic/uploadfile/',
		secureuri:false,
		uploadform: formname,
		dataType: 'json',
		fileUpload:true,
		success: function (data, status) {
			if (data.error == 0) {
				htm = '<img id="img_thumb_' + div_id + '" src="' + data.url + '" alt="" />'
				///
				jQuery("#success_img_"+div_id).html(data.message);
				jQuery("#success_img_"+div_id).show();
				///
				jQuery("#td_"+div_id).html(htm);
			}
			else {
				jQuery("#error_img_"+div_id).html(data.message);
				jQuery("#error_img_"+div_id).show();
			}
			///
			jQuery("#progress_"+div_id).hide();
			jQuery("#upload_form_"+div_id).show();
		},
		error: function (data, status, e, aa) {
			jQuery("#error_img_"+div_id).html(e);
			jQuery("#error_img_"+div_id).show();
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
	formname = document.getElementById('upload_form');
	///
	jQuery("#error_img").hide();
	jQuery("#success_img").hide();
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
					jQuery("#success_img").html(data.message);
					jQuery("#success_img").show();
					///
					document.location = '/puzzle/option/'+data.file+'/';
				}
				else {
					jQuery("#error_img").html(data.message);
					jQuery("#error_img").show();
				}
				///
				jQuery("#progress").hide();
				jQuery("#upload_form").show();
			},
			error: function (data, status, e, aa) {
				jQuery("#error_img").html(e);
				jQuery("#error_img").show();
				jQuery("#progress").hide();
				jQuery("#upload_form").show();
			}
		});
	}
	else {
		jQuery("#upload_form").show();
		jQuery("#error_img").html('Выберите изображение');
		jQuery("#error_img").show();
	}
}
