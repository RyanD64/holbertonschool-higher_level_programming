#!/usr/bin/node
// js script that print the addition of 2 numbers

function add (a, b) {
  return (a + b);
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
