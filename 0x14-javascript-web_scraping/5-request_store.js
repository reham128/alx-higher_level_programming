#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const webUrl = process.argv[2];
const fPath = process.argv[3];

request.get(webUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(fPath, body, 'utf-8', (err) => {
    if (err) console.error(err);
  });
});
