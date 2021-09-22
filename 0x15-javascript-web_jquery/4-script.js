$('DIV#toggle_header').click(function (e) {
  e.preventDefault();
  if ($('header').hasClass('red')) {
    $('header').toggleClass('green');
  } else {
    $('header').toggleClass('red');
  }
});
