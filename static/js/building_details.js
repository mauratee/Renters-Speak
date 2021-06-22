"use strict";

alert("JS is connected");

// Selects from violation-group in building_details.html
$("#violation-group").ready(function(){
  $("show_fewer_violations").click(function(){
    $("violation-list").slideUp();
  });
  $("show_more_violations").click(function(){
    $("violation-list").slideDown();
  });
});