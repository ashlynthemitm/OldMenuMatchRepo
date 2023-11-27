const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

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


//star ratings
const stars = document.querySelectorAll(".stars ion-icon");

//loop through stars NodeList
stars.forEach((star, index1) => {
    //event listener for when click event is triggered
    star.addEventListener("click", () => {
        console.log(clicked);
    });
});