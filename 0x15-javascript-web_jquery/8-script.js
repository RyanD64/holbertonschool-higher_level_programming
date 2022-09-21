window.$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const a in data.results) {
    window.$('#list_movies').append('<li>' + data.results[a].title + '</li>');
  }
});
