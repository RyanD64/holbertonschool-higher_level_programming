window.$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  window.$('#character').text(data.name);
});
