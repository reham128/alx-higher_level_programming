#!/usr/bin/node

const num = process.argv[2];
if (num === undefined || isNaN(num)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < Number(num)) {
    console.log('X'.repeat(Number(num)));
    i++;
  }
}
