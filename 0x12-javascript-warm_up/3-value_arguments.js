#!/usr/bin/node
const process = require('process');
const argv = process.argv;
if (argv[2]) {
  console.log(argv[2]); 
} else if (!argv[2]) {
  console.log('No argument');
}
