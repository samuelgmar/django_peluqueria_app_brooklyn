$(document).ready(function(){
	$('.next').click(function(){
		  var current = $(this).parent();
		  var next = $(this).parent().next();
		  $(".progress li").eq($("fieldset").index(next)).addClass("active");
		  current.hide();
		  next.show();
	})
	
	$('.previous').click(function(){
		  var current = $(this).parent();
		  var prev = $(this).parent().prev()
		  $(".progress li").eq($("fieldset").index(current)).removeClass("active");
		  current.hide();
		  prev.show();
	})
  })