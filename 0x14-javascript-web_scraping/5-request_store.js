#!/usr/bin/node

const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const file = process.argv[3];

req(url, (err, res, body) => {
  if (err) throw err;

  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
