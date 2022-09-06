#!/usr/bin/node
const num = parseInt(process.argv[2]);
function fac (num) {
  if (num < 0) return;
  if (num === 0 || isNaN(num)) return 1;
  return num * fac(num - 1);
}
console.log(fac(num));
