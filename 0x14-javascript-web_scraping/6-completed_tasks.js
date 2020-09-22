#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
const dict = {};

req(url, (err, res, body) => {
  if (err) throw err;
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      dict[`${task.userId}`] = (dict[`${task.userId}`] || 0) + 1;
    }
  }
  console.log(dict);
});
