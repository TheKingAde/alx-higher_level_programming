// Wait for the document to be ready
$(document).ready(function () {
  // Listen for a click event on INPUT#btn_translate
  $('#btn_translate').click(function () {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Fetch the translation from the API service
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
      // Display the translation in the DIV#hello element
      $('#hello').text(data.hello);
    });
  });

  // Listen for an Enter key press when the focus is on INPUT#language_code
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Enter key
      $('#btn_translate').click(); // Trigger the translation
    }
  });
});
