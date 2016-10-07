$(document).ready(function() {
  console.log('Ready');
  var $speed = $('.active.speed').children().text()

  $('.speed').on('click tap', function() {
    $('.speed').removeClass('active');
    $(this).addClass('active');
    $speed = $('.active.speed').children().text()
  })
  $(".arrow").on('mousedown vmousedown touchstart', function() {
    $(this).addClass('active');
    sendMove($(this).attr('id'), $speed);
  })

  $(".arrow").on('mouseup vmouseup mouseout touchend', function() {
    $(this).removeClass('active');
    sendMove('stop', $speed);
  })

})

function sendMove(direction, speed) {
  $.ajax('/move', {
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({
        direction: direction,
        speed: speed
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
