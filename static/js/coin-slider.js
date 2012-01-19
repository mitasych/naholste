(function($) {var params=new Array;
	var images=new Array;
	var interval=new Array;
	var imagePos=new Array;
	var appInterval=new Array;	
	var squarePos=new Array;	
	$.fn.coinslider=$.fn.CoinSlider=function(options){init=function(el){
			images[el.id]=new Array();
			imagePos[el.id]=0;
			squarePos[el.id]=0;
			params[el.id]=$.extend({},$.fn.coinslider.defaults,options);
			$.each($('#'+el.id+' img'),function(i,item){images[el.id][i]=$(item).attr('src');
			});
			$(el).css({background:'url('+images[el.id][0]+')',width:951,height:383,position:'relative',backgroundPosition:'top left'}).wrap("<div class='coin-slider' id='coin-slider-"+el.id+"' />");
			$('#'+el.id).append("<div class='cs-"+el.id+"' id='cs-"+el.id+"' style='width:100%;height:100%;left:0;top:0;position:absolute;background-position:0 0;'></div>");
			$('.cs-'+el.id).hover(function(){$('#cs-navigation-'+el.id).show();params[el.id].pause=true},function(){$('#cs-navigation-'+el.id).hide();params[el.id].pause=false});
			$('#coin-slider-'+el.id).append("<div id='cs-buttons-"+el.id+"' class='cs-buttons'></div>")
			for(k=1;k<images[el.id].length+1;k++){
				$('#cs-buttons-'+el.id).append("<a class='cs-button-"+el.id+"' id='cs-button-"+el.id+"-"+k+"'></a>")
			}
			$.each($('.cs-button-'+el.id),function(i,item){$(item).click(
				function(e){
					if($(this).hasClass('cs-active')){return false}
					else{$('.cs-button-'+el.id).removeClass('cs-active');
						$(this).addClass('cs-active');
						$.transition(el,i);
						$.transitionCall(el)
					}
				})
			})
			$.transitionCall(el)
			$('.cs-button-'+el.id).eq(0).addClass('cs-active');
			$('.banner').eq(imagePos[el.id]).css({opacity:1,left:-420}).animate({left:47},800,'easeOutBack')
		}
		$.transitionCall=function(el){
			clearInterval(interval[el.id]);	
			delay=params[el.id].delay;interval[el.id]=setInterval(function(){$.transition(el)},delay);
		}
		$.transition=function(el,direction){if(params[el.id].pause==true)return;
			squarePos[el.id]=0;
			$(el).css({'background-image':'url('+images[el.id][imagePos[el.id]]+')'});
			if(typeof(direction)=="undefined") imagePos[el.id]++;
			else if(direction=='prev') imagePos[el.id]--;
			else imagePos[el.id]=direction;
			if(imagePos[el.id]==images[el.id].length){imagePos[el.id]=0}
			if(imagePos[el.id]==-1){imagePos[el.id]=images[el.id].length-1}
			$('.cs-button-'+el.id).removeClass('cs-active');
			$('#cs-button-'+el.id+"-"+(imagePos[el.id]+1)).addClass('cs-active');
			$('.banner').animate({opacity:0},function(){appInterval[el.id]=setInterval(function(){$.appereance(el,0)})})
		};
		$.appereance=function(el,sid){
			if(squarePos[el.id]==1){clearInterval(appInterval[el.id]);return}
			$('#cs-'+el.id).css({opacity:0,'background-image':'url('+images[el.id][imagePos[el.id]]+')'}).stop().animate({opacity:1},1200,function(){$('.banner').eq(imagePos[el.id]).css({opacity:1,left:-420}).animate({left:47},800,'easeOutBack')});
			squarePos[el.id]++;
		};
	this.each (
		function(){init(this);}
	);
	};
	$.fn.coinslider.defaults={
		delay:6000,// delay between images in ms
		sDelay:0
	};	
})(jQuery);
$(window).load(function(){$('#coin-slider').coinslider()})