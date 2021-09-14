#!/usr/bin/node
const fd = require('fs');
const argv = process.argv;

fd.writeFile(argv[2], argv[3], (err, data) => {
  if (err) {
    console.log(err);
  }
});
