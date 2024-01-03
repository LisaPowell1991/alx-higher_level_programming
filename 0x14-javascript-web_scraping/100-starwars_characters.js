#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movieInfo = JSON.parse(body);

    for (const characterUrl of movieInfo.characters) {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character details:', charError);
        } else {
          const characterInfo = JSON.parse(charBody);
          console.log(characterInfo.name);
        }
      });
    }
  }
});
