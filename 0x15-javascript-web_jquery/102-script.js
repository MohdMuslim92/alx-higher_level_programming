// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Handle click event when #btn_translate is clicked
  $('#btn_translate').click(function () {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Make an AJAX request to fetch translation from the API
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
      // Display the translation of "Hello" in the HTML tag DIV#hello
      $('#hello').text(data.hello);
    }).fail(function (error) {
      // Handle errors if the request fails
      $('#hello').text('Error: Translation not found');
      console.error('Error:', error);
    });
  });
});
