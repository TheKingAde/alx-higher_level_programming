// Wait for the document to be ready
$(document).ready(function () {
  // Fetch the translation from the specified URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Extract the translated "hello" value
    const translatedHello = data.hello;

    // Display the translation in the DIV#hello element
    $('#hello').text(translatedHello);
  });
});
