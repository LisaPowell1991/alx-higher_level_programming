#!/usr/bin/node

const importedList = require('./100-data').list;

const newList = importedList.map((value, index) => value * index);

console.log(importedList);
console.log(newList);
