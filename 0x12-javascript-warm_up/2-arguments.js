#!/usr/bin/node
import { argv } from 'process';
if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else if (argv.length > 3) {
  console.log('Arguments found');
}
