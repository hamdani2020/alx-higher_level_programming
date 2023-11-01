const movieL = $('UL#list_movies');
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: (movies) => {
    $.each(movies.results, (i, movie) => {
      movieL.append('<li>' + movie.title + '</li>');
    });
  }
});
