#!/usr/bin/node
// js script that print a specific sentence if the first arg can be converted to an int

const num = parseInt(process.argv[2]);

if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
