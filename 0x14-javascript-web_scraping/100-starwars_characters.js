#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}`, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieInfo = JSON.parse(body);

    movieInfo.characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterInfo = JSON.parse(body);
          console.log(characterInfo.name);
        }
      });
    });
  }
});
