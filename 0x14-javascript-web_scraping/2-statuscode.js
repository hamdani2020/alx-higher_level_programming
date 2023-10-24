#!/usr/bin/node

const request = require('request');
// request
const url = process.argv[2];


request
  .get(url)
  .on('response', (response) => {
	  console.log('code: ' + response.statusCode);
  });
