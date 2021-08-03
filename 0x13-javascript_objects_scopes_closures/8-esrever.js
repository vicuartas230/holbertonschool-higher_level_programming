#!/usr/bin/node
exports.esrever = function (list) {
  const arrRev = [];
  let i = list.length - 1;
  let j = 0;
  while (i >= 0) {
    arrRev[j] = list[i];
    i--;
    j++;
  }
  return arrRev;
};
