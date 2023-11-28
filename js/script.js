//not in use but it's in the github so idk if i should delete it
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

//star ratings
const stars = document.querySelectorAll(".stars ion-icon");

//loop through stars NodeList
stars.forEach((star, index1) => {
    //event listener for when click event is triggered
    star.addEventListener("click", () => {
        console.log(clicked);
    });
});

function callPythonFunctions(funName){
    /*
    ajax link (paste jquery link at the end of html ) --> in doc --> https://code.jquery.com/jquery-3.6.4.min.js ??

    fetch('/call-python-functions') 
    .then(response => response.json()) 
    .then(data => console.log(data)) 
    .catch(error => console.error(error)); 
    */
   
    $.ajax ({
        type:'POST',
        url: '/call-python-functions',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify ({
            user_name: user_name,
            user_email: user_email,
            user_password: user_password,
            function: funName
            
            // include all data you need from the form input and or login page
        }),
        success: function (response) {
            console.log(response) // this returns an object reponse 
        },
        error: function (error) {
            console.log(error) // print the error from this call

        }
    });
}