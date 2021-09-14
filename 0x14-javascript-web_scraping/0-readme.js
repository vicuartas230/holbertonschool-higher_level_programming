#!/usr/bin/node
const fd = require('fs');
const argv = process.argv;

fd.readFile(argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
