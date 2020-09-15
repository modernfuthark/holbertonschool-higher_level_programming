#!/usr/bin/node

const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let holder = x; holder > 0; holder--) {
    console.log('X'.repeat(x));
  }
}
