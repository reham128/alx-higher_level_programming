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
  printAll(characters, 0);
});

function printAll (charc, i) {
  request(charc[i], function (error, response, body) {
    if (error) console.error(error);
    else {
      console.log(JSON.parse(body).name);
      if (i + 1 < charc.length) printAll(charc, i + 1);
    }
  });
}
