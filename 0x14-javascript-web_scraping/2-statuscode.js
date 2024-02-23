#!/usr/bin/node
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    // If an error occurred, print the error
    console.error(error);
  } else {
    // If no error occurred, print the status code
    console.log('code:', response.statusCode);
  }
});
