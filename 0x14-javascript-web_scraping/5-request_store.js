#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const fd = require('fs');

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fd.writeFile(argv[3], body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
