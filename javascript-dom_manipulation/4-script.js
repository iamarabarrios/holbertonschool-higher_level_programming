document.querySelector('#add_item').addEventListener('click', () => {
    const li = document.querySelector('.my_list');
    li.innerHTML += '<li>Item</li>';
});
