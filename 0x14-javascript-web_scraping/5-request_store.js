#!/usr/bin/node

const request = require('request');

const urlToRequest = process.argv[2];

const filePath = process.argv[3];

request(urlToRequest, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const fs = require('fs');
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
