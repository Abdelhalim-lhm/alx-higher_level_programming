#!/usr/bin/node
const Square0 = require('./5-square');

class Square extends Square0 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let txt = '';
      for (let j = 0; j < this.width; j++) {
        txt += c;
      }
      console.log(txt);
    }
  }
}

module.exports = Square;
