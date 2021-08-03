#!/usr/bin/node
exports.callMeMoby = function execs (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};
