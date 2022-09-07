#!/usr/bin/node
const SquareModel = require('./5-square');

class Square extends SquareModel {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let a = '';
      for (let j = 0; j < this.width; j++) a += (c === undefined) ? 'X' : c;
      console.log(a);
    }
  }
}

module.exports = Square;
