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

let loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    print('inside loginform event listener');
    let email = document.getElementById("login_email");
    let password = document.getElementById("login_password");
  
    if (email.value == "" || password.value == "") {
      alert("Ensure you input a value in both fields!");
    } else {
      // perform operation with form input
      result = callPythonUserFunctions('get-user-pass', {'email':email, 'password':password});
      if(result.success){
        window.alert(result);
        //window.location.href = "home.html";
      }else{
        alert("Incorrect Email/Passowrd Combo");
      }
    }
  });

  let registrationForm = document.getElementById("registrationForm");

  registrationForm.addEventListener("submit", (e) => {
      e.preventDefault();

      let name = document.getElementById('register_name');
      let email = document.getElementById("register_email");
      let password = document.getElementById("register_password");
    
      if (name.value == "" || email.value == "" || password.value == "") {
        alert("Ensure you input a value in all fields!");
      } else {
        // perform operation with form input
        result = callPythonUserFunctions('create-user', {'name' : name,'email':email, 'password':password});
        if(result != []){
            window.location.href = "home.html";
        }
    }
    });

console.log('Wrapper:', wrapper);
console.log('Register Link:', registerLink);

//star ratings
const stars = document.querySelectorAll(".stars ion-icon");

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

function checkLogin(){
    
}


async function callPythonUserFunctions(funName, data_dict){
    try{
        const response = await fetch('/api/call-python-user-functions', {
            mode: "cors", // no-cors, *cors, same-origin
            cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'include',
            method: 'POST',
            headers: {'Content-Type' : 'application/json'},
            
            body: JSON.stringify({
                'data_dict': data_dict,
                'function': funName            
            }),
        }) 
    
        if(response.ok) {
            response.json()
            .then(function(response) {
                console.log('back from request');
                console.log(response);
                if(response.success){
                    return response;
                }else{
                    return response;
                }
            });
        }
        else {
            throw Error('Something went wrong');
        }
    }
    catch(error) {
        console.log(error);
    }
    /*
   //.then(data => console.log(data)) 
    $.ajax ({
        type:'GET',
        url: '/call-python-user-functions',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({
            /*user_name: user_name,
            email: document.getElementById(),
            user_password: user_password,
            user_allergens: user_allergens,
            user_id: user_id,
            rest_id: rest_id,
            rating: rating,
            data_dict: data_dict,
            function: funName
            
            // include all data you need from the form input and or login page
        }),
        success: function (response) {
            console.log(response) // this returns an object reponse 
            if(response.success){
                return response.records;
            }else{
                return []
            }
        },
        error: function (error) {
            console.log(error) // print the error from this call

        }
    });*/
}

//the array that is going to be on the table
    //static tables would be in the braces but since we're getting dynamic tables from the api 
    //i deleted them
	/*var myArray = [            
        {'menuid':'1', 'menuitem':'Margherita Pizza', 'allergen':'Dairy, Gluten', 'cooktime':'15', 'foodtype':'Italian', 'restaurantid':'162', 'restaurantid':'162', 'restaurantname':'Casa Italia', 'address':'666 Pecan Lane', 'distanceinmiles':'2.1', 'restauranttype':'Italian', 'averagepricescore':'3.4', 'none':'None'},
        {'menuid':'2', 'menuitem':'Spaghetti', 'allergen':'Gluten', 'cooktime':'15', 'foodtype':'Italian', 'restaurantid':'162', 'restaurantid':'162', 'restaurantname':'Casa Italia', 'address':'666 Pecan Lane', 'distanceinmiles':'2.1', 'restauranttype':'Italian', 'averagepricescore':'3.4', 'none':'None'},

    ]*/

    var myArray;

    //ajax gets information from the api
    //url is empty because that's where the link to the api goes
    //use inspect console in the browser to check for the actual name of the array and change
    //'response' in myArray=response to 'response.data' (data is whatever holds the array)
    function temp(){
        $.ajax({
            method: 'GET',
            url:'/call-python-mr-functions',
            success: function(response){
                myArray = response.records
                buildTable(myArray)
                console.log(myArray)
            }
        })

        //search keyup function
        //pulls up what you're searching for (value) when you type
        $('#search-input').on('keyup', function(){
            var value = $(this).val()
            console.log('Value:', value)
            var data = searchTable(value, myArray)
            buildTable(data)
        })

        buildTable(myArray)
    }
    //function that takes in the value from above and array
    function searchTable(value, data){
        var filteredData = []

        //loop through the array and in every single value that contains whatever the input is
        for (var i = 0; i < data.length; i++){
            //change everything to lowercase so case sensitivity doesn't occur
            value = value.toLowerCase()
            //name we're filtering by
            var menuitem = data[i].menuitem.toLowerCase()

            //conditional
            if (name.includes(value)){
                filteredData.push(data[i])
            }
        }

        return filteredData
    }

    //builds the table
	function buildTable(data){
		var table = document.getElementById('myTable')

        //table gets completely rebuilt each time
        table.innerHTML = ''

		for (var i = 0; i < data.length; i++){
            // //create row with temperate literal, allows you 
            //to make rows without having to constantly concatenate
            //${data[i].menuid is basically what connects each piece of info to its label
            //this is the format each element in the array has to be in to use this method
            //if you have another way you can def use that (watch out for the quotations)
            //{'menuid':'1', 'menuitem':'Margherita Pizza', 'allergen':'Dairy, Gluten', 'cooktime':'15', 'foodtype':'Italian', 'restaurantid':'162', 'restaurantid':'162', 'restaurantname':'Casa Italia', 'address':'666 Pecan Lane', 'distanceinmiles':'2.1', 'restauranttype':'Italian', 'averagepricescore':'3.4', 'none':'None'},
			var row = `<tr>
                            <td>${data[i].menuid}</td>
                            <td>${data[i].menuitem}</td>
                            <td>${data[i].allergen}</td>
                            <td>${data[i].cooktime}</td>
                            <td>${data[i].foodtype}</td>
                            <td>${data[i].restaurantid}</td>
                            <td>${data[i].restaurantid}</td>
                            <td>${data[i].restaurantname}</td>
                            <td>${data[i].address}</td>
                            <td>${data[i].distanceinmiles}</td>
                            <td>${data[i].restauranttype}</td>
                            <td>${data[i].averagepricescore}</td>
                            <td>${data[i].none}</td>
					  </tr>`
			table.innerHTML += row


		}
	}

function callPythonMRFunctions(funName){
    /*
    ajax link (paste jquery link at the end of html ) --> in doc --> https://code.jquery.com/jquery-3.6.4.min.js ??

    fetch('/call-python-functions') 
    .then(response => response.json()) 
    .then(data => console.log(data)) 
    .catch(error => console.error(error)); 
    */
   
    $.ajax ({
        type:'POST',
        url: '/call-python-mr-functions',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify ({
            /*menu_item: menu_item,
            menu_allergens: menu_allergens,
            cook_time: cook_time,
            type: type,
            rest_name: rest_name,
            distance: distance,
            rest_type: rest_type,
            price: price_score,*/
            data_dict: data_dict,
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