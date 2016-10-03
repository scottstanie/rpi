$(document).ready(function() {
  console.log('Ready');

})

function fetch_new_results(first_id) {
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
