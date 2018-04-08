$(function(){
	$(window).scroll(function(){
		if($(window).scrollTop() > 100){
			$('.navbar').css("padding", "10px 16px");
			$('.navbar-brand').css("font-size", "1.5rem");
		}
		else{
			$('.navbar').css("padding", "24px 16px");
			$('.navbar-brand').css("font-size", "32px");
		}
	});
});