#!/usr/bin/node

$('document').ready(function () {
  const ele = $('div#hello');
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
    ele.append(`<p>${data.hello}</p>`);
  });
});
