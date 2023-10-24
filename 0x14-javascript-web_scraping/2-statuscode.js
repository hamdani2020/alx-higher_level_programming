#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
//request here

request
  .get(url)
  .on('response', (response) => {
	  console.log('code: ' + response.statusCode);
  });
