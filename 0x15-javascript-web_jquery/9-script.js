window.$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
  window.$('#hello').text(data.hello);
});
