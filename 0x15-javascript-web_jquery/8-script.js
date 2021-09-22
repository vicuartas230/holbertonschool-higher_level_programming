$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json',
  function (data) {
    let text;
    for (const item in data.results) {
      text = '<li>' + data.results[item].title + '</li>';
      $('UL#list_movies').append(text);
    }
  }
);
