#!/usr/bin/node
const process = require('process');
const args = process.argv;
const fs = require('fs');
fs.readFile(args[2], 'utf-8', function (_err, data) {
  fs.readFile(args[3], 'utf-8', function (err2, data2) {
    const str = data + '\n' + data2 + '\n';
    fs.writeFile(args[4], str, function () {});
  });
});
