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

//asynchronous request to server
fetch('/api/data')
    .then(response => {
        if (!response.ok) {
            throw new Error('HTTP error! Status: ${response.status}');
        }
        return response.json();
    })
    .then(data => {
        //update html with data from server
        document.getElementById('result').innerText = data.message;
    })
    .catch(error => console.error('Error:', error));
