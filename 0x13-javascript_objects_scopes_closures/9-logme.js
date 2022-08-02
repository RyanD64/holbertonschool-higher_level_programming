#!/usr/bin/node
// js script that return the number of arguments already printed and their value
let d = 0;
exports.logMe = function (item) {
  console.log(d + ': ' + item);
  d++;
};
