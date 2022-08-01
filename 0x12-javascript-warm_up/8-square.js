#!/usr/bin/node
// js script that print a square

const num = parseInt(process.argv[2]);

if (num) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
