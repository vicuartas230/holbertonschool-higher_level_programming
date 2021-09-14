#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const listFilms = JSON.parse(body).results;
  let cont = 0;
  for (let index = 0; index < listFilms.length; index++) {
    if (listFilms[index].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      cont++;
    }
  }
  console.log(cont);
});
