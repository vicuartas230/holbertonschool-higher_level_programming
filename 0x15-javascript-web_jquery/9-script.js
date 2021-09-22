document.addEventListener('DOMContentLoaded', function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr',
    function (data) {
      console.log(data);
      $('DIV#hello').html(data.hello);
    }
  );
});
