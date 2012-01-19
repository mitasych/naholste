/***********************************************************************************************************************
DOCUMENT: includes/javascript.js
DEVELOPED BY: Ryan Stemkoski
COMPANY: Zipline Interactive
EMAIL: ryan@gozipline.com
PHONE: 509-321-2849
DATE: 2/26/2009
DESCRIPTION: This is the JavaScript required to create the accordion style menu.  Requires jQuery library
************************************************************************************************************************/

$(document).ready(function() {
	
	/********************************************************************************************************************
	SIMPLE ACCORDIAN STYLE MENU FUNCTION
	********************************************************************************************************************/	
	$('div.accordionButton').click(function() {
		$('div.accordionContent').slideUp('normal');	
		$(this).next().slideDown('normal');
		///
		$('div.accordionButton').css({"font-weight":"normal"});
		$(this).css({"font-weight":"bold"});
	});
	
	/********************************************************************************************************************
	CLOSES ALL DIVS ON PAGE LOAD
	********************************************************************************************************************/	
	$("div.accordionContent").hide();

});
