"use strict";

alert("JS is connected")

// var myModal = document.getElementById('myModal')
// var myInput = document.getElementById('myInput')

var myModal = new bootstrap.Modal(document.getElementById('myModal'), options)


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
