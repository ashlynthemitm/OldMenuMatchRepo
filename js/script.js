const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');
const searchForm = document.querySelector('form');
const searchInput = document.querySelector('#search');
const resultsList  = document.querySelector('#results');

//listeners for login and register
registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
});

//listener for x close icon
iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
});

//listener for search
searchForm.addEventListener('submit', (e) => {
    e.preventDefault();
})


function changePage(page) {
    // You can load content dynamically based on the page parameter
    // For simplicity, let's just update the content div with a simple message
    var contentDiv = document.getElementById('content');
    
    switch (page) {
        case 'home':
            contentDiv.innerHTML = '<h2>Welcome to the Home Page!</h2>';
            break;
        case 'about':
            contentDiv.innerHTML = '<h2>About Us</h2><p>We are a fantastic company!</p>';
            break;
        case 'contact':
            contentDiv.innerHTML = '<h2>Contact Us</h2><p>Reach out to us at contact@example.com</p>';
            break;
        default:
            contentDiv.innerHTML = '<h2>Page not found</h2>';
    }
}
