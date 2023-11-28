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

/* When the user clicks on allergen button,
toggle between hiding and showing the dropdown content */
function dropdown() {
    document.getElementById("dropdown-content").classList.toggle("show");
}
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

/* When the user clicks on food type button,
toggle between hiding and showing the dropdown content */
function fooddropdown() {
    document.getElementById("foodtype-content").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.fooddropbtn')) {
      var dropdowns = document.getElementsByClassName("fooddropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }