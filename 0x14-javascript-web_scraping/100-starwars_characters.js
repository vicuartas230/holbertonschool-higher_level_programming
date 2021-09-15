#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const chars = JSON.parse(body).characters;
  chars.map(element => request(element, (error, response, body) => {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(body).name);
  }));
});
