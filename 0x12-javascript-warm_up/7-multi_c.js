#!/usr/bin/node
// js script that print x times c is fun

const num = parseInt(process.argv[2]);

if (num) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
