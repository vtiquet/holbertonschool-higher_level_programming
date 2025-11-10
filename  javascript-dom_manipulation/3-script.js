const headerElement = document.querySelector('header');

const clickElement = document.getElementById('toggle_header');

if (headerElement && clickElement) {
  clickElement.addEventListener('click', () => {
    if (headerElement.classList.contains('red')) {
      headerElement.classList.remove('red');
      headerElement.classList.add('green');
    } else if (headerElement.classList.contains('green')) {
      headerElement.classList.remove('green');
      headerElement.classList.add('red');
    }
  });
}
