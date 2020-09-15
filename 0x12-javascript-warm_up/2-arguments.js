#!/usr/bin/node

/* console.log(process.argv.length); */

if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
