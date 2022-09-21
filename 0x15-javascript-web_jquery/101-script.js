window.$().ready(function () {
  window.$('#add_item').click(function () {
    window.$('ul.my_list').append('<li>Item</li>');
  });
  window.$('#remove_item').click(function () {
    window.$('ul.my_list li:last-child').remove();
  });
  window.$('#clear_list').click(function () {
    window.$('ul.my_list').empty();
  });
});
