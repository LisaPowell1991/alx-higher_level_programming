#!/usr/bin/node

const firstArgument = process.argv[2];

const parsedInteger = parseInt(firstArgument);

if (isNaN(parsedInteger)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedInteger}`);
}
