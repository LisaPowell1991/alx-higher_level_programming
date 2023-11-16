#!/usr/bin/node

const firstArgument = process.argv[2];

const x = parseInt(firstArgument);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
