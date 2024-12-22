#!/usr/bin/node
const fs = require('fs');
const f1 = fs.readFileSync(process.argv[2], 'utf-8');
const f2 = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], f1 + f2, 'utf-8');
