#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const dicc = {};

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const task = JSON.parse(body).filter(function (item) {
    return item.completed === true;
  });
  for (let index = 0; index < task.length; index++) {
    if (dicc[task[index].userId]) {
      dicc[task[index].userId]++;
    } else {
      dicc[task[index].userId] = 1;
    }
  }
  console.log(dicc);
});
