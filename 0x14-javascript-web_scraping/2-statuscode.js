#!/usr/bin/node

const request = require('request');

const urlToRequest = process.argv[2];

request(urlToRequest, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(response.statusCode);
  }
});
