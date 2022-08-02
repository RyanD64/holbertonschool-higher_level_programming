#!/usr/bin/node
// js script that concat two files
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (fileA && fileB && fileC) {
  const fs = require('fs');
  let txt = '';
  txt += fs.readFileSync(fileA) + '\n';
  txt += fs.readFileSync(fileB) + '\n';
  fs.writeFileSync(fileC, txt);
}
