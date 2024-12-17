#!/usr/bin/node
// print "C is fun" multiple times
const num = parseInt(process.argv[2]);
if (Number.isNaN(num)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
