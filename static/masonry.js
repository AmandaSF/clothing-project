$('.display').imagesLoaded()
  .always( function( instance ) {

  	var $display = $('.display').masonry({
	  // options
	  itemSelector: '.item',
	  columnWidth: '.item',
	  percentPosition: true
	});



    console.log('all images loaded');
  });