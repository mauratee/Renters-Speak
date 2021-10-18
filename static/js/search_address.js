"use strict";

// alert("JS is connected");


// make ajax request to "/autocomplete" route as user types address in search bar
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
            console.log(ui.item.value);
        }
    });
})