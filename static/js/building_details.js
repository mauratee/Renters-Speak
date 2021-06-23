"use strict";

alert("JS is connected");

// Selects from violation-group in building_details.html
$("document").ready(function(){
  $("#show_fewer_violations").click(function(){
    $("#first-two-violations").slideUp();
  });
  $("#show_more_violations").click(function(){
    $("#first-two-violations").slideDown();
  });
});

// Selects from write-a-review button in building_details.html
// and send to write_review.html page
$("#write-a-review").on("click"), () => {
    window.location.replace("/write_review")
};