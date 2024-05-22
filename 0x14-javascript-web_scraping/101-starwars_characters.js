#!/usr/bin/node

const request = require('request');
const idMovie = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${idMovie}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  printAllCharacters(characters, 0);
});

function printAllCharacters (ch, idx) {
  request(ch[idx], function (error, response, body) {
    if (error) console.error(error);
    else {
      console.log(JSON.parse(body).name);
      if (idx + 1 < ch.length) printAllCharacters(ch, idx + 1);
    }
  });
}
