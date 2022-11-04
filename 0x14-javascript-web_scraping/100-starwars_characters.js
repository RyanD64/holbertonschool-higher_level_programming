#!/usr/bin/node
// script that prints the number of movies where was Wedge Antilles

const axios = require('axios');

axios
  .get('https://swapi-api.hbtn.io/api/films' + process.argv[2])
  .then(async (result) => {
    for (const characters of result.characters.data) {
      await axios.get(characters).then((result) => {
        console.log(result.data.name);
      });
    }
  })
  .catch((error) => {
    console.log(`code: ${error.response.status}`);
  });
