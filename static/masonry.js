// var $display = $('.display').masonry({
//   // options
//   itemSelector: '.item',
//   columnWidth: '.item',
//   percentPosition: true
// });


// // layout Masonry after each image loads
// $display.imagesLoaded().progress( function() {
//   $display.masonry('layout');
// });


// ( function( $ ) {
// var $container = $('.display');
// //layout Masonry again after all images have loaded
// $container.imagesLoaded( function() {
// $container.masonry();
// });})( jQuery );

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