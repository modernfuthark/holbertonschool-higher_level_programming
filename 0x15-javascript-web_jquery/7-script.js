#!/usr/bin/node

const ele = $('div#character');

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  ele.append(`<p>${data.name}</p>`);
});
