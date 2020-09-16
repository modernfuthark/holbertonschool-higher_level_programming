#!/usr/bin/node

exports.add = function (a, b) {
  const n1 = parseInt(a);
  const n2 = parseInt(b);
  if (n1 && n2) {
    return n1 + n2;
  } else {
    return NaN;
  }
};
