#!/usr/bin/node

const argumentList = process.argv.slice(2);

if (argumentList.length === 0 || argumentList.length === 1) {
  console.log('0');
} else {
  const integers = argumentList.map(arg => parseInt(arg));

  const sortedIntegers = integers.sort((a, b) => b - a);

  const secondBiggest = sortedIntegers[1];

  console.log(secondBiggest);
}
