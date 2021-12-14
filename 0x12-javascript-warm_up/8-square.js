#!/usr/bin/node
const argv = require('process').argv;
let sides = parseInt(argv[2]);
let line = '';
let exes = 0;

if (isNaN(sides)) {
  console.log('Missing size');
} else if (sides > 0) {
  while (exes !== sides) {
    line += 'X';
    exes++;
  }
  while (sides !== 0) {
    console.log(line);
    sides--;
  }
}
