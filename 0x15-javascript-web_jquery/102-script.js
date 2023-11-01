window.onload = () => {
    $('INPUT#btn_translate').click(() => {
      const langu = $('INPUT#language_code').val();
      $.ajax({
        url: 'https://fourtonfish.com/hellosalut/?lang=' + langu,
        type: 'POST',
        success: (translation) => {
          $('DIV#hello').text(translation.hello);
        },
        error: () => {
          console.log('There is an error loading orders');
        }
      });
    });
  };
