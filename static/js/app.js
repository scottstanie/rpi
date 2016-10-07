$(document).ready(function() {
  console.log('Ready');
  $(".arrow").on('mousedown vmousedown touchstart', function() {
    $(this).addClass('active');
    sendMove($(this).attr('id'));
  })

  $(".arrow").on('mouseup vmouseup mouseout touchend', function() {
    $(this).removeClass('active');
    sendMove('stop');
  })

})

function sendMove(direction) {
  $.ajax('/update_results', {
      type: 'GET',
      contentType: 'application/json',
      data: JSON.stringify({
        first_id: first_id
      }),
      success: function(data) {
        console.log(data);
      },
      error: function(data) {
        console.log('Error');
        console.log(data);
      },
  });
  return true;
}
