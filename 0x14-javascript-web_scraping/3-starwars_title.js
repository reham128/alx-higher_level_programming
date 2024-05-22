#!/usr/bin/node

const request = require('request');
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
