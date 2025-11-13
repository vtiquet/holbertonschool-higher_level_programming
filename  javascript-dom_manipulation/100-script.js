document.addEventListener('DOMContentLoaded', () => {
  const addItemBtn = document.getElementById('add_item');
  const removeItemBtn = document.getElementById('remove_item');
  const clearListBtn = document.getElementById('clear_list');
  const myList = document.querySelector('.my_list');

  if (addItemBtn && myList) {
    addItemBtn.addEventListener('click', () => {
      const newListItem = document.createElement('li');
      newListItem.textContent = 'Item';
      myList.appendChild(newListItem);
    });
  }

  if (removeItemBtn && myList) {
    removeItemBtn.addEventListener('click', () => {
      if (myList.lastElementChild) {
        myList.removeChild(myList.lastElementChild);
      }
    });
  }

  if (clearListBtn && myList) {
    clearListBtn.addEventListener('click', () => {
      myList.innerHTML = '';
    });
  }
});
