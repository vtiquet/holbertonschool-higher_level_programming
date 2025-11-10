document.addEventListener('DOMContentLoaded', () => {
  const listMoviesElement = document.getElementById('list_movies');

  const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

  if (listMoviesElement) {
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        const films = data.results;

        films.forEach(film => {
          const newListItem = document.createElement('li');
          newListItem.textContent = film.title;
          listMoviesElement.appendChild(newListItem);
        });
      })
      .catch(error => {
        console.error('Fetch error:', error);
        const errorItem = document.createElement('li');
        errorItem.textContent = 'Error loading movies.';
        listMoviesElement.appendChild(errorItem);
      });
  }
});
