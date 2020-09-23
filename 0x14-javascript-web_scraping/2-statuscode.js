#!/usr/bin/node

const url = process.argv[2];
const req = require('request');

req(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
