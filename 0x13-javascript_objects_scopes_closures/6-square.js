#!/usr/bin/node
// js script that create a class square
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.height; a++) {
      for (let a = 0; a < this.width; a++) {
        process.stdout.write(c);
      }
      console.log('');
    }
  }
}

module.exports = Square;
