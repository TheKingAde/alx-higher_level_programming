// Wait for the document to be ready
$(document).ready(function () {
  // Select the DIV#update_header element
  $('#update_header').click(function () {
    // Update the text of the <header> element to "New Header!!!"
    $('header').text('New Header!!!');
  });
});
