// Wait for the document to be ready
$(document).ready(function () {
  // Fetch the character data from the specified URL
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extract the character name
    const characterName = data.name;

    // Display the character name in the DIV#character element
    $('#character').text(characterName);
  });
});
