"use strict";

alert("JS is connected");

// Add event listener input type to detect any change to input field
$("#search_nyc_address").on("input", () => {

    // Get user input from search form
    const formData = {
        text: $("#search_nyc_address").val(),
    };

    $.get("/server_route", )
})