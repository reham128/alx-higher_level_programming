#!/usr/bin/node

const arg0 = process.argv[2];
if (arg0 === undefined) {
  console.log('No argument');
} else {
  console.log(arg0);
}
