#!/usr/bin/node

function add (a, b) {
  const n1 = parseInt(a);
  const n2 = parseInt(b);
  if (n1 && n2) {
    console.log(n1 + n2);
  } else {
    console.log(NaN);
  }
}

add(process.argv[2], process.argv[3]);
