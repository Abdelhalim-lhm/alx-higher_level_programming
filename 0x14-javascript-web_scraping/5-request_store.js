#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf8', error => {
    if (error) {
      console.error(error);
    }
  });
});
