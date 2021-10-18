"use strict";


// alert("JS is connected");

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



// use JS to gather values from HTML form (AJAX lecture)
// prevent default in behavior in JS, (look at AJAX lecture)
// jQuery.post
// to prevent request going to server, do submit manually in JS
// JS makes request, gets response which contains output from server route
// return json object from /login route instead of return redirect
// hardcode dictionary to return from route
