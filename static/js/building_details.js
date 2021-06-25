"use strict";

alert("JS is connected");

// Selects from violation-group in building_details.html
$("document").ready(function(){
  $("#show_fewer_violations").click(function(){

    console.log("show fewer violations click happened")
    $("#first-two-violations").slideUp();
    
    console.log($("#first-two-violations"))
  });
  $("#show_more_violations").click(function(){
    console.log("show more violations click happened")
    $("#first-two-violations").slideDown();
  });
});

// Hides next-violations in building_details
$("#next-violations").hide();


// Selects from write-a-review button in building_details.html
// and send to write_review.html page
$("#write-a-review").on("click"), () => {
    window.location.replace("/write_review")
};



$(document).ready(function(){
  $("#violations-info-trigger")
    .mouseenter(function() {
      $(this).find("span").effect("highlight", {color:"#FFFF00"}, 1000);
    })
    .mouseleave(function() {
      $(this).find("span").removeClass("highlight");
    });
});

document.getElementById("violations-info").style.display = "none"; 

$(document).ready(function(){
  $("#violations-info-trigger").on("click", function(){
    $("#violations-info").slideToggle();
  });
});


// $.get("/violations_by_class.json", (res) => {
//   console.log(res);
// });

console.log($("#violation-class").data("chart"))

Chart.defaults.elements.arc.backgroundColor = ["#5E309c", "#56b1e7", "#5F19e6"]  ;

// Chart.js test
const testChart = new Chart(
    $('#violation-class'),
    {
    type: 'doughnut',
    data:($("#violation-class").data("chart"))
    }
);