#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let j = 0; j < this.width; j++) {
      console.log(`${c}`.repeat(this.height));
    }
  }
}

module.exports = Square;
