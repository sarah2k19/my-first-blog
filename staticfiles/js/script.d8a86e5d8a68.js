/*$(document).ready(function () {
    $(document).click(function () {
        $('div').fadeOut('fast');
    });
});


$( function() {
    $( "post" ).sortable();
    $( "post" ).disableSelection();
  } );
*/


$( function() {
    $( "div" ).sortable();
    $( "div" ).disableSelection();
    $( "h2" ).sortable({items: '> h2:not(.date)'});
  } );

/*
$(document).ready(function(){

  $('.post').hover(
    function(){
        $(this).css('background-color', '#ffebe6');
    },
    function(){
        $(this).css('background-color', '#ffe6c1');
    }
  );
});
*/

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
