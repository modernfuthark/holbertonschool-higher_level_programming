#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
const char = 'https://swapi-api.hbtn.io/api/people/18/';

req(url, (err, res, body) => {
  if (err) throw err;

  let count = 0;
  JSON.parse(body).results.forEach(function (itm, idx) {
    if (itm.characters.includes(char)) {
      count++;
    }
  });
  console.log(count);
});
