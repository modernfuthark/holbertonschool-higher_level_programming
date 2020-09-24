#!/usr/bin/node

const ele = $('ul#list_movies');

$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  const films = data.results;
  for (const film of films) {
    ele.append(`<li>${film.title}</li>`);
  }
});
