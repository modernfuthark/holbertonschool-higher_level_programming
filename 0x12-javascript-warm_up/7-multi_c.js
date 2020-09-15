#!/usr/bin/node

const goal = process.argv[2];

if (!parseInt(goal)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < goal; i++) {
    console.log('C is fun');
  }
}
