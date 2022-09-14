#!/usr/bin/node
// script that prints the number of movies where was Wedge Antilles
const axios = require('axios');
const adress = process.argv[2];

axios
  .get(`${adress}`)
  .then((result) => {
    let count = 0;
    for (const film of result.data.results) {
      for (const listActors of film.characters) {
        if (listActors.includes('people/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  })
  .catch((error) => {
    console.error(error);
  });
