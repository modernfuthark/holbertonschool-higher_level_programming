#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let j = 0; j < this.width; j++) {
        console.log(`${c}`.repeat(this.height));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Rectangle;
module.exports = Square;
