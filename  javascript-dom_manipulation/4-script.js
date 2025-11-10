const addItemElement = document.getElementById('add_item');

const listElement = document.querySelector('.my_list');

if (addItemElement && listElement) {
  addItemElement.addEventListener('click', () => {
    const newListItem = document.createElement('li');
    newListItem.textContent = 'Item';

    listElement.appendChild(newListItem);
  });
}
