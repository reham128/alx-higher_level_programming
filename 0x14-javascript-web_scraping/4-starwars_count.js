#!/usr/bin/node

const request = require('request');
const movieUrl = process.argv[2];
const charId = 18;

request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    let count = 0;

    movies.forEach(movie => {
      movie.characters.forEach(character => {
        if (character.includes(`/${charId}/`)) {
          count++;
        }
      });
    });

    console.log(count);
  }
});
