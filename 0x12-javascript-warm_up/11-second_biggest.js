#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  let i = 2;
  const arr = [];
  let j = 0;
  while (i < args.length) {
    arr[j] = parseInt(args[i]);
    i++;
    j++;
  }
  arr.sort(function (a, b) {
    return a - b;
  });
  console.log(arr[arr.length - 2]);
}
