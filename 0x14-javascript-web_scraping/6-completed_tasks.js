#!/usr/bin/node
// script that prints the number of movies where was Wedge Antilles
const axios = require('axios');

const list = {};
let value;
axios
  .get(process.argv[2])
  .then((result) => {
    for ([, value] of Object.entries(result.data)) {
      if (value.completed === true) {
        if (list[value.userId] === undefined) {
          list[value.userId] = 0;
        }
        list[value.userId] += 1;
      }
    }
    console.log(list);
  })
  .catch((error) => {
    console.error(error);
  });
