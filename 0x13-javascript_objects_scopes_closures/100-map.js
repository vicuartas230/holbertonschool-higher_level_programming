#!/usr/bin/node
const list = require('./100-data').list;
let i = 0;
const newList = list.map(function (item) {
  return item * i++;
});
console.log(list);
console.log(newList);
