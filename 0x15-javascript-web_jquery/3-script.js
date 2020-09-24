#!/usr/bin/node

const head = $('div#red_header');

head.click(function () {
  $(this).addClass('red');
});
