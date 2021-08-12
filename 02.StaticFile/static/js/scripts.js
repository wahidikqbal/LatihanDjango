$(window).scroll(function(){
	var scroll = $(window).scrollTop();


	document.getElementById("body").style.marginTop = (-50 - 0.80*scroll) + "px";

	if(scroll >=200){
		$("#navScroll").addClass("bg-dark");
	} else {
		$("#navScroll").removeClass("bg-dark");
	}
});
