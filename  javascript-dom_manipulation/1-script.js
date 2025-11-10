const headerElement = document.querySelector('header');

const clickElement = document.getElementById('red_header');

if (headerElement && clickElement) {
  clickElement.addEventListener('click', () => {
    headerElement.style.color = '#FF0000';
  });
}
