#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const args = process.argv;
  let first = args[2];
  let second = args[3];
  let i = 2;

  while (args[i]) {
    if (args[i] > first) {
      second = first;
      first = args[i];
    } else if (args[i] < first && args[i] > second) {
      second = args[i];
    }
    i++;
  }
  console.log(second);
}
