#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const starwarsApi = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(starwarsApi, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const starwarsInfo = JSON.parse(body);
    console.log(starwarsInfo.title);
  }
});
