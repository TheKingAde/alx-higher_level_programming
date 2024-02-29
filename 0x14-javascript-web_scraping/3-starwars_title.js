#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL for the Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    // If an error occurred, print the error
    console.error(error);
  } else {
    // If no error occurred, parse the body of the response into a JavaScript object
    const data = JSON.parse(body);

    // Print the title of the movie
    console.log(data.title);
  }
});
