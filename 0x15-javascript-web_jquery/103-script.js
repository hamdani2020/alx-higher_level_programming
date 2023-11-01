function postLangu () {
    const langu = $('INPUT#language_code').val();
    $.ajax({
      type: 'POST',
      url: 'https://www.fourtonfish.com/hellosalut/hello/' + langu,
      success: (translation) => {
        $('DIV#hello').text(translation.hello);
      },
      error: () => {
        console.log('There is an error loading orders');
      }
    });
  }
  
  window.onload = () => {
    $('INPUT#btn_translate').focus(() => {
      $('INPUT#btn_translate').keypress((key) => {
        if (key.which === 13) {
          postLangu();
        }
      });
      $('INPUT#btn_translate').click(() => {
        postLangu();
      });
    });
  };
