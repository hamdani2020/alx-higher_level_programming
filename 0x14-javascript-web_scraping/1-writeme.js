#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const dataWrite = process.argv[3];

fs.writeFile(filePath, dataWrite, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
