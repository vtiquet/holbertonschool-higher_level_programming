document.addEventListener('DOMContentLoaded', () => {
  const translateBtn = document.getElementById('btn_translate');
  const languageCodeSelect = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');
  const apiUrlBase = 'https://hellosalut.stefanbohacek.com/';

  if (translateBtn && languageCodeSelect && helloDiv) {
    translateBtn.addEventListener('click', () => {
      const langCode = languageCodeSelect.value;

      if (!langCode) {
        helloDiv.textContent = 'Please select a language.';
        return;
      }

      const fullUrl = `${apiUrlBase}?lang=${langCode}`;

      fetch(fullUrl)
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          return response.json();
        })
        .then(data => {
          if (data.hello) {
            helloDiv.textContent = data.hello;
          } else {
            helloDiv.textContent = 'Translation not found.';
          }
        })
        .catch(error => {
          console.error('Fetch error:', error);
          helloDiv.textContent = 'Error fetching translation.';
        });
    });
  }
});
