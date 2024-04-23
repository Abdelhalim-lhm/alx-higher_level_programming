#!/usr/bin/node
const fs = require('node:fs');
fs.readFile(process.argv[2], 'utf8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
