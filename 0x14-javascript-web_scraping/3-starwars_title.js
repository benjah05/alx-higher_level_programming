#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + episode, function (err, response, body) {
	if (err) {
		console.log(err);
	} else if (response.statusCode === 200) {
		const responseJSON = JSON.parse(body);
		console.log(responseJSON.title);
	} else {
		console.log('Error code: ' + response.statusCode);
	}
});
