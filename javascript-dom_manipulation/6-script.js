const characterElement = document.getElementById('character');

const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

if (characterElement) {
  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      characterElement.textContent = data.name;
    })
    .catch(error => {
      console.error('Fetch error:', error);
      characterElement.textContent = 'Error loading character.';
    });
}
