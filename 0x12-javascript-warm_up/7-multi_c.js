#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (!parseInt(args[2])) {
  console.log('Missing number of occurrences');
}
let i = 0;
while (i < parseInt(args[2])) {
  console.log('C is fun');
  i++;
}
