#!/usr/bin/node
const arg = process.argv[2];
const x = parseInt(arg);

if (isNaN(x) || x <= 0) {
  console.log('Missing number of occurrences');
} else {
  let output = '';
  for (let i = 0; i < x; i++) {
    output += 'C is fun\n';
  }
  console.log(output.slice(0, -1));
}
