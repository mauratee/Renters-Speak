"use strict";


alert("JS is connected");

// Selects from login-form in login.html
$("#login-form").on("submit", (evt) => {
    evt.preventDefault();

    // Get user input from login form
    const formData = {
        email: $("#email-field").val(),
        password: $("#password-field").val()
    };

    // Send formData to the server
    $.post("/login", formData, (res) => {
        // Display response from the server if user not logged in
        if (res === "Please enter correct email and password or register for a new account.") {
            alert(res)
        }
        // If user logged in, redirect to another page
        else {
            window.location.replace("/write_review")}   
    });
});






// const loginForm = document.querySelector("form");

// loginForm.addEventListener("submit", (evt) => {
//     evt.preventDefault();

//     alert("Success, you are logged in!")
// });

// var myModal = document.getElementById('myModal')
// var myInput = document.getElementById('myInput')

// var myModal = new bootstrap.Modal(document.getElementById('myModal'), options)

// const button = document.querySelector("login_button");

//         button.addEventListener('click', () => {
//           alert('Success, you are logged in!');
//         });

// $("login-button").on("click", (evt) => {
    //     evt.preventDefault();
    
    //     alert("Success, you are logged in!")
    // });

// $('#delivery-form').on('submit', (evt) => {
//     evt.preventDefault();
          
//     // Get user input from a form
//     const formData = {
//         city: $('#city-field').val(),
//         address: $('#adr-field').val()
//         };
          
//     // Send formData to the server (becomes a query string)
//     $.get('/delivery-info.json', formData, (res) => {
//         // Display response from the server
//         alert(`This will cost $${res.cost}`);
//         alert(`This will arrive in ${res.days} day(s)`);
//         });
// });


// myModal.addEventListener('shown.bs.modal', function () {
//   myInput.focus()
// })


// use JS to gather values from HTML form (AJAX lecture)
// prevent default in behavior in JS, (look at AJAX lecture)
// jQuery.post
// to prevent request going to server, do submit manually in JS
// JS makes request, gets response which contains output from server route
// return json object from /login route instead of return redirect
// hardcode dictionary to return from route

// if it's an sQLAlchemy object
