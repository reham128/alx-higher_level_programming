#!/usr/bin/node
const list = require('./100-data.js').list;
const newArr = list.map(item, indx);
console.log(list);
console.log(newArr);
