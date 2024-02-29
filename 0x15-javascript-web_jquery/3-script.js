// Wait for the document to be ready
$(document).ready(function () {
  // Select the DIV#red_header element
  $('#red_header').click(function () {
    // Add the class "red" to the <header> element
    $('header').addClass('red');
  });
});
