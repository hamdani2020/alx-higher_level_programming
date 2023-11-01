$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  type: 'GET',
  success: (character) => {
    $('DIV#character').text(character.name);
  }
});
