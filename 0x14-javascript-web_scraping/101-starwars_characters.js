#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request.get(character, function (error, response, body) {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  }
});
