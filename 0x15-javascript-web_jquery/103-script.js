// Wait for the DOM content to be fully loaded
$(document).ready(function () {
  // Function to fetch translation
  function fetchTranslation () {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Make an AJAX request to fetch translation from the API
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`,
      method: 'GET',
      dataType: 'json'
    })
      .done(function (data) {
      // Display the translation of "Hello" in the HTML tag DIV#hello
        if (data.hello) {
          $('#hello').text(data.hello);
        } else {
          $('#hello').text('Translation not found for the given language code.');
        }
      })
      .fail(function (xhr, status, error) {
      // Handle errors if the request fails
        $('#hello').text('Error: ' + error);
        console.error('Error:', error);
      });
  }

  // Handle click event when #btn_translate is clicked
  $('#btn_translate').click(fetchTranslation);

  // Handle keypress event when ENTER key is pressed in #language_code input field
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      // 13 is the ASCII code for ENTER key
      fetchTranslation();
    }
  });
});
