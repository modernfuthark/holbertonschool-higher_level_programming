#!/usr/bin/node

const head = $('div#toggle_header');

head.click(function () {
  if (!$(this).attr('class')) { /* Don't know if they wanted this, but w/e */
    $(this).addClass('red');
  } else if ($(this).attr('class') === 'red') {
    $(this).removeClass('red');
    $(this).addClass('green');
  } else if ($(this).attr('class') === 'green') {
    $(this).removeClass('green');
    $(this).addClass('red');
  }
});
