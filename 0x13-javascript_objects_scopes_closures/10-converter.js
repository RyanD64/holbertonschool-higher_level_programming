#!/usr/bin/node
// js script that convert a number from base 10 to another base
exports.converter = function (base) {
  return function (decimal) {
    return decimal.toString(base);
  };
};
