#!/usr/bin/node
const argv = require('process').argv;
const value = parseInt(argv[2]);
if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number:', value);
}
