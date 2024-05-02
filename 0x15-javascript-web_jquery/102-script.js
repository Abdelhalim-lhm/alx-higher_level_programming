$(document).ready(function () {
  $('#btn_translate').click(function () {
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
  });
});
