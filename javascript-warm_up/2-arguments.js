#!/usr/bin/node
const numArgs = process.argv.slice(2);

if (numArgs.length === 0) {
  console.log('No argument');
} else if (numArgs.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
