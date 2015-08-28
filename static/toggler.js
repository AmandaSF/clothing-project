$( "button" ).click(function() {
  $( ".display" ).toggle();
  $("button").text() === "See What Users Are Sharing" ?  $("button").text("See What Users Need"): $("button").text("See What Users Are Sharing"); 

});

$( ".fa-bars").on("click", function() {
	if ( $(".dropdown > div").is(":hidden") ) {
		$(".dropdown > div").slideDown();
	} else {
		$(".dropdown > div").slideUp();
	}
	
})
