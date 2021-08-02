#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
const process = require('process');
const args = process.argv;
if (!args[2]) {
  console.log(1);
} else {
  console.log(factorial(args[2]));
}
