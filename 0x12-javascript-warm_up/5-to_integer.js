#!/usr/bin/node
// convert arg to number
const numArg = parseInt(process.argv[2]);
if (Number.isNaN(numArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numArg);
}
