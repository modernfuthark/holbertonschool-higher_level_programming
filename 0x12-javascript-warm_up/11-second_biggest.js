#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv;
  let first = args[2];
  let second = args[3];
  let i = 2;

  while (args[i]) {
    const n = parseInt(args[i]); /* Without this, 53 > 5253 */
    if (n > first) {
      second = first;
      first = n;
    }
    if (n < first && n > second) {
      second = n;
    }
    i++;
  }
  console.log(second);
}
