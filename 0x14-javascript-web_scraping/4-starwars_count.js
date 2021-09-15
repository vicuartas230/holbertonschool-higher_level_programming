#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const listFilms = JSON.parse(body).results;
  const cont = listFilms.filter(function (item) {
    return item.characters.includes('https://swapi-api.hbtn.io/api/people/18/');
  }).length;
  console.log(cont);
});
