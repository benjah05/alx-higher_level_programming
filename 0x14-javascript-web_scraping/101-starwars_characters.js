#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + episode, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    orderedPrint(characters, 0);
  }
});

function orderedPrint (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        orderedPrint(characters, index + 1);
      }
    }
  });
}
