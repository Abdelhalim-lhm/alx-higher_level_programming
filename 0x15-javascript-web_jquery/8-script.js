$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      const films = data.results;
      for (const film of films) {
        $('ul#list_movies').append(`<li>${film.title}</li>`);
      }
    },
    error: function (xhr, status, error) {
      console.error('Error:', error);
    }
  });
});
