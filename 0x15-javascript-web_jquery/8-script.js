// Wait for the document to be ready
$(document).ready(function () {
  // Make an HTTP GET request to the SWAPI URL
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Extract the movie titles from the response
    const movieTitles = data.results.map(movie => movie.title);

    // Create a list item for each movie title
    movieTitles.forEach(title => {
      const listItem = $('<li>').text(title);
      $('#list_movies').append(listItem);
    });
  });
});
