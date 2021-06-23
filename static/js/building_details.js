"use strict";

alert("JS is connected");

// Selects from violation-group in building_details.html
var violationList = {{ violation_list|safe }}
console.log(violationList)

$("document").ready(function(){
  $("#show_fewer_violations").click(function(){
    $("#first-two-violations").slideUp();
  });
  $("#show_more_violations").click(function(){
    $("#first-two-violations").slideDown();
  });
});