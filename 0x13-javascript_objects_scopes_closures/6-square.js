#!/usr/bin/node
const Square = required('./5-square');
class Square extends Square {
  constructor(size) {
    super(size);
  }

  charPrint(c) {
    if (c == undefined) {
      c = 'X';
    }

    for (let = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
