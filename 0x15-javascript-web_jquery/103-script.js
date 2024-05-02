$(document).ready(function () {
  function Translate () {
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + $('#language_code').val(),
      method: 'GET',
      success: function (data) {
        $('#hello').text(data.hello);
      },
      error: function (xhr, status, error) {
        console.error('Error:', error);
      }
    });
  }

  $('#btn_translate').click(Translate);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      Translate();
    }
  });
});
