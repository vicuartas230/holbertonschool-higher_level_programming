#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const dicc = {};

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const biggest = JSON.parse(body)[JSON.parse(body).length - 1].userId;
  for (let index = 1; index <= biggest; index++) {
    dicc[index.toString()] = JSON.parse(body).filter(function (item) {
      return item.userId === index;
    }).filter(function (task) {
      return task.completed === true;
    }).length;
  }
  console.log(dicc);
});
