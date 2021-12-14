#!/usr/bin/node
const argv = require('process').argv;
let multiplier = parseInt(argv[2]);
if (isNaN(multiplier)) {
  console.log('Missing number of occurences');
} else if (multiplier > 0) {
  while (multiplier !== 0) {
    console.log('C is fun');
    multiplier--;
  }
}
