#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (!parseInt(args[2])) {
  console.log('Missing size');
}
let i = 0;
while (i < parseInt(args[2])) {
  console.log('X'.repeat(parseInt(args[2])));
  i++;
}
