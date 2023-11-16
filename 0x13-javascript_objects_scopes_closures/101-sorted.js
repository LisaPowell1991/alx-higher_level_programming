#!/usr/bin/node

const importedDict = require('./101-data').dict;

const occurrencesById = {};

for (const userId in importedDict) {
  const occurrences = importedDict[userId];

  if (!occurrencesById[occurrences]) {
    occurrencesById[occurrences] = [];
  }

  occurrencesById[occurrences].push(parseInt(userId));
}
console.log(occurrencesById);
