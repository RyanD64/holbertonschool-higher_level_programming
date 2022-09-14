#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const axios = require('axios');
const fs = require('fs');

axios
  .get(process.argv[2])
  .then((result) => {
    if (result.status === 200) {
      fs.writeFile(`./${process.argv[3]}`, result.data, { flag: 'w+' }, (error) => {
        if (error) {
          console.error(error);
        }
      });
    }
  })
  .catch((error) => {
    console.log(error);
  });
