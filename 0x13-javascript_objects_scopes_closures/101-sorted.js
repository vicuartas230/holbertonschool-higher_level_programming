#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
let occurences = [];
const a = Object.entries(dict);
if (!a.length) {
  process.exit();
}
let b = Object.keys(newDict);
let search = a[0][1];
let i = 0;
let j = 0;
while (j < a.length) {
  i = j;
  if (!b.includes(search.toString())) {
    while (i < a.length) {
      if (b.includes(search.toString())) {
        break;
      }
      if (a[i][1] === search) {
        occurences.push(a[i][0]);
      }
      i++;
    }
    newDict[search] = occurences;
    b = Object.keys(newDict);
  }
  j++;
  if (j < a.length - 1) {
    search = a[j][1];
  }
  occurences = [];
}
console.log(newDict);
