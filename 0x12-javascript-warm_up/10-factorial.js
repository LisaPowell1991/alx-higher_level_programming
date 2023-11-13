#!/usr/bin/node

function calculateFactorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * calculateFactorial(n - 1);
  }
}

const firstArgument = process.argv[2];

const factorialNum = parseInt(firstArgument);

if (isNaN(factorialNum)) {
  console.log('1');
} else {
  const result = calculateFactorial(factorialNum);
  console.log(`${result}`);
}
