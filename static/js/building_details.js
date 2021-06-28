"use strict";

alert("JS is connected");



// Set display of violation-list to none as default
$(".violation-list").hide()

// Set display of violation alert to none, will display when clicked through end of list
document.getElementById("violation-alert").style.display = "none";

// Set display of end-of-list alert to none, will display when clicked through end of list
document.getElementById("end-of-list").style.display = "none";


// Shows violations a few at a time
$(".violation-list").slice(0,4).show();
$("#show-more-violations").on("click", function (evt) {
  evt.preventDefault();
  $(".violation-list:hidden").slice(0,4).slideDown();
  // If no more violations are hidden in list, flash alert
  if ($(".violation-list:hidden").length == 0) {
    $("#violation-alert").show();
  }
});

// Hides violations a few at a time
$("#show-fewer-violations").on("click", function (evt) {
  evt.preventDefault();
  $(".violation-list:visible").slice(0,4).slideUp();
  // If all violations hidden, flash alert
  if ($(".violation-list:visible").length == 0) {
    $("#end-of-list").show();
  }
})

// Shows all remaining hidden violations
$("#show-all-violations").on("click", function (evt) {
  // console.log("we clicked show all violations");
  evt.preventDefault();
  if ($(".violation-list:hidden").length != 0) {
    $(".violation-list:hidden").slideDown();
  }
  else {
    $(".violation-list:visible").slideUp();
  }
});

// Set display to none for "write-a-review-group"
document.getElementById("write-a-review-group").style.display = "none"; 

// Selects from write-a-review button in building_details.html
// and displays write-a-review-group on click
$(document).ready(function(){
  $("#write-a-review").on("click", function(){
    $("#write-a-review-group").slideToggle();
  });
});


// Add highlight to NYC Housing Code Violations text on mouseover
$(document).ready(function(){
  $("#violations-info-trigger")
    .mouseenter(function() {
      $(this).find("span").effect("highlight", {color:"#FFFF00"}, 1000);
    })
    .mouseleave(function() {
      $(this).find("span").removeClass("highlight");
    });
});


// Set default display of violations-info to none
document.getElementById("violations-info").style.display = "none"; 

// Slide toggle to show violations info on click of trigger
$(document).ready(function(){
  $("#violations-info-trigger").on("click", function(){
    $("#violations-info").slideToggle();
  });
});


// Add highlight to Violation Class text on mouseover
$(document).ready(function(){
  $("#violations-class-info-trigger")
    .mouseenter(function() {
      $(this).find("span").effect("highlight", {color:"#FFFF00"}, 1000);
    })
    .mouseleave(function() {
      $(this).find("span").removeClass("highlight");
    });
});


// Set display attribute of violations-class-info to none
$(".violations-class-info").hide();

// On click, display violations-class-info
$(document).ready(function(){
  $("#violations-class-info-trigger").on("click", function(){
    $("#violations-class-info").slideToggle();
  });
});



console.log($("#violation-class").data("chart"))

Chart.defaults.elements.arc.backgroundColor = ["#5E309c", "#56b1e7", "#5F19e6"]  ;

// construct Chart.js doughnut graph for violaiton classes
const testChart = new Chart(
    $('#violation-class'),
    {
    type: 'doughnut',
    data:($("#violation-class").data("chart"))
    }
);