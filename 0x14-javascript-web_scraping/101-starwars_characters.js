#!/usr/bin/node

const request = require('request');
const idMovie = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${idMovie}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
