#!/usr/bin/node
// js script that compute and print a factorial

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2).sort((a, b) => a - b);
  console.log(list[list.length - 2]);
}
