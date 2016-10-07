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

  var fired = false;
  $(document).on("keydown", function (e) {
    if (!fired) {
      fired = true;
      switch(e.which) {
          case 37: // left
            $('#left').addClass('active')
            sendMove('left', $speed)
          break;

          case 38: // up
            $('#up').addClass('active')
            sendMove('up', $speed)
          break;

          case 39: // right
            $('#right').addClass('active')
            sendMove('right', $speed)
          break;

          case 40: // down
            $('#down').addClass('active')
            sendMove('down', $speed)
          break;

          default: return; // exit this handler for other keys
      }
    }
    e.preventDefault(); // prevent the default action (scroll / move caret)
  });

  $(document).on("keyup", function (e) {
    if (fired) {
      fired = false;
      $('.arrow').removeClass('active');  // Uncolor all arrows
      sendMove('stop', $speed);
      e.preventDefault(); // prevent the default action (scroll / move caret)
    }
  });

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
