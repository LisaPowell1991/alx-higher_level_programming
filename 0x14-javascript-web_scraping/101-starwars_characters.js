#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) { console.error(error); }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error(characterError);
      } else {
        const characterData = JSON.parse(characterBody);
        console.log(characterData.name);
      }
    });
  });
});
