#!/usr/bin/node

const sqrC = require('./5-square');
class Square extends sqrC {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let i;
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
