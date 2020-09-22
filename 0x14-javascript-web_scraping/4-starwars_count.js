#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
const char = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;

req(url, (err, res, body) => {
  if (err) throw err;

  for (const film of JSON.parse(body).results) {
    if (film.characters.includes(char)) {
      count++;
    }
  }
  console.log(count);
});
