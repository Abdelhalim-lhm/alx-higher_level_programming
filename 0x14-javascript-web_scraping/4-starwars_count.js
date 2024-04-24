#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  data.results.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(18)) {
        count += 1;
      }
    });
  });
  console.log(count);
});
