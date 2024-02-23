#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the URL and the file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    // If an error occurred, print the error
    console.error(error);
  } else {
    // If no error occurred, write the body of the response to the file
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        // If an error occurred during writing, print the error
        console.error(err);
      }
    });
  }
});
