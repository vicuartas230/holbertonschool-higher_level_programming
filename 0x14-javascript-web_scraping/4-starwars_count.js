#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const listFilms = JSON.parse(body).results;
  const film = listFilms.map(item => item.characters);
  const chars = film.map(x => x.includes('https://swapi-api.hbtn.io/api/people/18/'));
  const done = chars.filter(element => element).length;
  console.log(done);
});
