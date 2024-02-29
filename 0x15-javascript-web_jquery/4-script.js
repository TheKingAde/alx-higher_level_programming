// Wait for the document to be ready
$(document).ready(function () {
  // Select the DIV#toggle_header element
  $('#toggle_header').click(function () {
    // Toggle the class of the <header> element
    $('header').toggleClass('red green');
  });
});
