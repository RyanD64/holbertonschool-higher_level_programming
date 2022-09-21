window.$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  window.$('DIV#hello').append(data.hello);
});
