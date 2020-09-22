#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}/`;

req(url, (err, res, body) => {
  if (err) throw err;
  for (const character of JSON.parse(body).characters) {
    req(character, (err, res, body) => {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  }
});
