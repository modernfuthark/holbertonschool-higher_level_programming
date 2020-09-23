#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
/* const char = 'https://swapi-api.hbtn.io/api/people/18/'; */
let count = 0;

req(url, (err, res, body) => {
  if (err) throw err;

  for (const film of JSON.parse(body).results) {
    for (const char of film.characters) {
      if (char.includes('/people/18')) {
        count++;
      }
    }
  }
  console.log(count);
});
