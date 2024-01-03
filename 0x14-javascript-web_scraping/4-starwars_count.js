#!/usr/bin/node

const request = require('request');

const starwarsApiUrl = process.argv[2];

request(starwarsApiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const starwarsInfo = JSON.parse(body);

    let wedgeAntillesCount = 0;

    starwarsInfo.results.forEach(movie => {
      const wedgeAntilles = movie.characters.find(character => character.endsWith('/18/'));

      if (wedgeAntilles) { wedgeAntillesCount++; }
    });
    console.log(wedgeAntillesCount);
  }
});
