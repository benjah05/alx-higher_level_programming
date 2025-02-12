#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    const characters = responseJSON.characters;
    for (const character of characters) {
      request.get(character, function (err, res, c) {
        if (err) {
          console.log(err);
        } else if (res.statusCode === 200) {
          const info = JSON.parse(c);
          console.log(info.name);
        }
      });
    }
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
