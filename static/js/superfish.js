(function($){$.fn.superfish=function(op){var sf=$.fn.superfish,c=sf.c,$arrow = $(['<span class="',c.arrowClass,'"></span>'].join('')),over=function(){var $$=$(this),menu=getMenu($$);clearTimeout(menu.sfTimer);$$.showSuperfishUl().siblings().hideSuperfishUl()},out=function(){var $$=$(this),menu=getMenu($$),o=sf.op;clearTimeout(menu.sfTimer);menu.sfTimer=setTimeout(function(){o.retainPath=($.inArray($$[0],o.$path)>-1);$$.hideSuperfishUl();if(o.$path.length&&$$.parents(['li.',o.hoverClass].join('')).length<1){over.call(o.$path)}},o.delay)},getMenu=function($menu){var menu=$menu.parents(['ul.',c.menuClass,':first'].join(''))[0];sf.op=sf.o[menu.serial];return menu},addArrow=function($a){$a.addClass(c.anchorClass).append($arrow.clone())};return this.each(function(){var s=this.serial=sf.o.length;var o=$.extend({},sf.defaults,op);o.$path=$('li.'+o.pathClass,this).slice(0,o.pathLevels).each(function(){$(this).addClass([o.hoverClass,c.bcClass].join(' ')).filter('li:has(ul)').removeClass(o.pathClass)});sf.o[s]=sf.op=o;$('li:has(ul)',this)[($.fn.hoverIntent&&!o.disableHI)?'hoverIntent':'hover'](over,out).each(function(){if(o.autoArrows)addArrow($('>a:first-child',this))});var $a=$('a',this);$a.each(function(i){var $li=$a.eq(i).parents('li')})}).each(function(){var menuClasses=[c.menuClass];$(this).addClass(menuClasses.join(' '))})};var sf=$.fn.superfish;sf.o=[];sf.op={};sf.c={bcClass:'sf-breadcrumb',menuClass:'sf-js-enabled',anchorClass:'sf-with-ul',arrowClass:'sf-sub-indicator',shadowClass:'sf-shadow'};sf.defaults={hoverClass:'sfHover',pathClass:'overideThisToUse',pathLevels:1,delay:800,animation:{height:'show'},speed:'normal',autoArrows:false,disableHI:false};$.fn.extend({hideSuperfishUl:function(){var o=sf.op,not=(o.retainPath===true)?o.$path:'';o.retainPath=false;var $ul=$(['li.',o.hoverClass].join(''),this).add(this).not(not).removeClass(o.hoverClass).find('>ul').hide().parent()
if($(this).parent().parent().is('li')){
					$(this).find('>span').stop().animate({height:0,top:15,left:'50%',width:0})
					$(this).find('>ul>li>span').css({height:0,top:15,left:'50%',width:0})
				}
				else {
					$(this).not('.current').stop().animate({backgroundPosition:'50% 52px'})
					$(this).find('>ul>li>span').css({height:0,top:15,left:'50%',width:0})
					$(this).find('>ul>li>ul>li>span').css({height:0,top:15,left:'50%',width:0})
				};return this},showSuperfishUl:function(){var o=sf.op,$ul=this.addClass(o.hoverClass).find('>ul:hidden');$ul.animate(o.animation,o.speed);return this}})})(jQuery);
$(function(){
	$('.sf-menu').superfish().find('ul li').not('.current').append('<span></span>')
	.hover(
		function(){
			$(this).find('>span').stop().animate({height:29,top:0,left:0,width:'100%'})
		},
		function(){
			if($(this).hasClass('sfHover'))return
			else $(this).find('>span').stop().animate({height:0,top:15,left:'50%',width:0})
		}
	)
	$('.sf-menu>li').not('.current').hover(function(){$(this).stop().animate({backgroundPosition:'50% -72px'})},function(){$(this).not('.sfHover').stop().animate({backgroundPosition:'50% 52px'})})
})