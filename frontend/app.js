const menu = document.querySelector('#mobile-menu')
const menuLinks = document.querySelector('.navbar__menu')

menu.addEventListener('click',function() {
    menu.classList.toggle('is-active')
    menuLinks.classList.toggle('active')
})


const imageBox = document.querySelector('.image-box');
const img = document.createElement('img');
img.src = 'path-to-your-image.jpg'; // Replace with your image path
img.alt = 'Description of Image';
img.className = 'image';
imageBox.appendChild(img);
