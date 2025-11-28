document.addEventListener('DOMContentLoaded', () => {
  const helloElement = document.getElementById('hello');
  const apiUrl = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  if (helloElement) {
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        if (data.hello) {
          helloElement.textContent = data.hello;
        } else {
          helloElement.textContent = 'Translation not found.';
        }
      })
      .catch(error => {
        console.error('Fetch error:', error);
        helloElement.textContent = 'Error fetching translation.';
      });
  }
});
