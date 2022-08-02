#!/usr/bin/node
// js script that import an array and compute a new array
const a = require('./100-data').list;
console.log(a);
console.log(a.map((x, y) => x * y));
