$(function(){
	tabs.init();
});	
tabs = {
	init : function(){
		$('.tabs').each(function(){
			$(this).find('.tab-content').hide();
			$($(this).find('ul.nav .selected a').attr('href')).fadeIn(300);
			$(this).find('ul.nav li').click(function(){if($(this).hasClass('selected')){return false}
			else{
				$(this).parents('.tabs').find('.tab-content').hide();
				$($(this).find('>a').attr('href')).fadeIn(300);
				$(this).addClass('selected').siblings().removeClass('selected');
				return false;}
			});
		});
	}
}