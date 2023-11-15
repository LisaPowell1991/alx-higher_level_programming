#!/usr/bin/node

const fs = require('fs');

const contentA = fs.readFileSync(process.argv[2], 'utf-8');
const contentB = fs.readFileSync(process.argv[3], 'utf-8');

const combinedContent = `${contentA}${contentB}`;

fs.writeFileSync(process.argv[4], combinedContent);
