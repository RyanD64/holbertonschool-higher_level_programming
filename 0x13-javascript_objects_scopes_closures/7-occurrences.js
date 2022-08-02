#!/usr/bin/node
// js script that return the number of occurences in a list
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (let j = 0; j < list.length; j++) {
    if (list[j] === searchElement) {
      i++;
    }
  }
  return i;
};
