const headerElement = document.querySelector('header');

const updateHeaderElement = document.getElementById('update_header');

if (headerElement && updateHeaderElement) {
  updateHeaderElement.addEventListener('click', () => {
    headerElement.textContent = 'New Header!!!';
  });
}
