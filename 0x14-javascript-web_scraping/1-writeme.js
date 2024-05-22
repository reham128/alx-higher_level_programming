#!/usr/bin/node

const fs = require('fs');
const fPath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(fPath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
