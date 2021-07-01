"use strict";

// alert("JS is connected");


// // Add event listener input type to detect any change to input field
// $("#search_nyc_address").on("input", () => {

//     // Get user input from search form, save in dictionary
//     const formData = {
//         text: $("#search_nyc_address").val(),
//     };

//     // Send formData to the server
//     $.get("/autocomplete", formData, (res) => {
//         for item in res () =>
//             var optionNode = document.createElement("option");
//             optionNode.value = "//address1//";
//             optionNode.appendChild(document.createTextNode("//firstaddresslabel//"));
//             document.getElementById("addresses").appendChild(optionNode);
//     })
// })

$(function() {
    $("#search_nyc_address").autocomplete({
        source:function(request, response) {
            $.getJSON("/autocomplete",{
                q: request.term, // in flask, "q" will be the argument to look for using request.args
            }, function(data) {
                response(data.matching_results); // matching_results from jsonify
                "<span class='ui-state-highlight'>$&</span>";
            });
        },
        minLength: 1,
        select: function(event, ui) {
            console.log(ui.item.value); // not in your question, but might help later
        }
    });
})