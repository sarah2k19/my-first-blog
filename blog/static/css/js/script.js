$( function() {
    $( "div" ).sortable();
    $( "div" ).disableSelection();
    $( "h2" ).sortable({items: '> h2:not(.date)'});
  } );


$(document).ready(function(){

  $('.post').hover(
    function(){
        $(this).fadeTo(500, 0.7);
    },
    function(){
        $(this).fadeTo(500, 1.0);
    }
  );
});
