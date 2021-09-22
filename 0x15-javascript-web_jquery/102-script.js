document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function (e) {
    e.preventDefault();
    const text = $('INPUT#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/?cc=' + text,
      function (data) {
        $('DIV#hello').html(data.hello);
      }
    );
  });
});
