#!/usr/bin/node

const ele = $('div#add_item');

ele.click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
