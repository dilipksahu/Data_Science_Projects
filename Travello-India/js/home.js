

$(window).scroll(function(){
	if($(this).scrollTop() > 0){
		$('.scroll').addClass("sticky");
	}
	else{
		$('.scroll').removeClass("sticky");
	}
});

// $(window).ready(function(){
// 	$(".img-zone").hover(function(){
// 		$(this).animate({"opacity":"0.5","height":"300px","width":"300px"});
// 	}, function(){ 
// 		$(this).animate({"opacity":"1","height":"150px","width":"300px"})
// 	});
// });

