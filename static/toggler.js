$( "button.items_toggle" ).click(function() {
  $( ".display" ).toggle();

  $('.display').imagesLoaded()
  .always( function( instance ) {

  	var $display = $('.display').masonry({
	  // options
	  itemSelector: '.item',
	  columnWidth: '.item',
	  percentPosition: true
	});

  });



  $("button.items_toggle").text() === "See What Users Are Sharing" ?  $("button.items_toggle").text("See What Users Need"): $("button.items_toggle").text("See What Users Are Sharing"); 

});

$( ".fa-bars").on("click", function() {
	if ( $(".dropdown > div").is(":hidden") ) {
		$(".dropdown > div").slideDown();
	} else {
		$(".dropdown > div").slideUp();
	}
	
})

$( "button.user_toggle" ).click(function() {
  $( ".display" ).toggle();

    $('.display').imagesLoaded()
  .always( function( instance ) {

  	var $display = $('.display').masonry({
	  // options
	  itemSelector: '.item',
	  columnWidth: '.item',
	  percentPosition: true
	});

  });

  $("button.user_toggle").text() === "Click for Shared Items" ?  $("button.user_toggle").text("Click for Requested Items"): $("button.user_toggle").text("Click for Shared Items"); 
});

$( ".flash_message" ).fadeOut(5000);
