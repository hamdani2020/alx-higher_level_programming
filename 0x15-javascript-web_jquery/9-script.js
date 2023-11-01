$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  type: 'POST',
  success: (translation) => {
    $('DIV#hello').text(translation.hello);
  },
  error: () => {
    console.log('This an error loading orders');
  }
});
