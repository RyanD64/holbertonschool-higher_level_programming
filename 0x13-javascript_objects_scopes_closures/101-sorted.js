#!/usr/bin/node
// js script that imports a dict of occurrs by user id and computes a dict of user ids by occurr
const dict = require('./101-data').dict;
const list = {};
for (const i in dict) {
  if (list[dict[i]] === undefined) {
    list[dict[i]] = [];
  }
  list[dict[i]].push(i);
}
console.log(list);
