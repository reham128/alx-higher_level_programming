#!/usr/bin/node
const argA = Number(process.argv[2]);
const argB = Number(process.argv[3]);

function add (a, b) {
  const result = a + b;
  console.log(result);
}
add(argA, argB);
