#!/usr/bin/node
const Squar = require('./5-square');
module.exports = class Square extends Squar {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.height));
        i++;
      }
    }
  }
};
