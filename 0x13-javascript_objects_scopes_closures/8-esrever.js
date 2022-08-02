#!/usr/bin/node
// js script that return the reversed version of a list
exports.esrever = function (list) {
  const tsil = [];
  for (let a = list.length - 1; a >= 0; a--) {
    tsil.push(list[a]);
  }
  return tsil;
};
