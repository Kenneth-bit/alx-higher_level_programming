#!/usr/bin/node
import { argv } from 'process';

const args = argv.length - 2;
if (args === 0) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Argument found');
} else if (args > 1) {
  console.log('Arguments found');
}
