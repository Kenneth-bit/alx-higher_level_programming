#!/usr/bin/node
const argv = require('process').argv;
let side = parseInt(argv[2]);
let line = 'X';


/*if (isNaN(sides)) {
  console.log('Missing size');
} else if (sides > 0) {
  for (i = 1; i <= sides; i++){
    for (j = 1; j <= sides; j++){
      console.log(line)
    }
    console.log('');
  }
}*/

for(i = 1; i <= side; i++){
  for(j = 1; j <= side; j++){
    console.log("*");
    }
  console.log("\n"); 
  }
