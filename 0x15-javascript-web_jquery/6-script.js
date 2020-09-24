#!/usr/bin/node

const ele = $('div#update_header');

ele.click(function () {
  $('header').text('New Header!!!');
});
