#!/usr/bin/node
// script that  prints the title of a Star Wars movie
const axios = require('axios').default;

axios
  .get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function () {
    console.log('error');
  });
