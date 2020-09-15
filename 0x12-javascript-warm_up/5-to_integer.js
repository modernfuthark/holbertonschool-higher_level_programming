#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (num) {
  console.log(`My number: ${num}`); /* I like this inline variable replacement method */
} else {
  console.log('Not a number');
}
