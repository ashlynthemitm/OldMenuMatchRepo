//one of the event listeners isn't working, allegedly it's register-link, the star rating isn't working because of it, idk what is wrong with it

//login and register starts
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
//login and register ends

console.log('Wrapper:', wrapper);
console.log('Register Link:', registerLink);

//star ratings
const stars = document.querySelectorAll('.stars ion-icon');

//loop through stars NodeList
stars.forEach((star, index1) => {
    //event listener for when click event is triggered
    star.addEventListener("click", () => {
        //loop through the "stars" Nodelist again
        stars.forEach((star, index2) => {
            //add "active" class to the clicked star and any stars with
            //a lower index and remove the "active" class from any stars with a higher index
            index1 >= index2 ? star.classList.add("active") : star.classList.remove("active")
        });
    });
});

/* document.onsubmit() {
    var user_name = document.querySelector(value="user_name")
    ... var user_password ..
    var isAdmin = False
    temp_allergen = []
    var allergen = document.querySelctor(value="user_allergen") stars.forEach --> temp_allergen

}
*/ 