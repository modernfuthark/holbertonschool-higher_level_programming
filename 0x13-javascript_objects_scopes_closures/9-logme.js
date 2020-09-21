#!/usr/bin/node

let runs = 0;

exports.logMe = function (item) {
  console.log(`${runs}: ${item}`);
  runs++;
};
