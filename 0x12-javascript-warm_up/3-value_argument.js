#!/usr/bin/node
// js script that print the first argument passed to it

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
