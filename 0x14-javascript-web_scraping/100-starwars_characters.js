#!/usr/bin/node

const request = require('request');
const idOfMovie = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${idOfMovie}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movie = JSON.parse(body);

  movie.characters.forEach(characterUrl => {
    request.get(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error(characterError);
        return;
      }
      const character = JSON.parse(characterBody);

      console.log(character.name);
    });
  });
});
