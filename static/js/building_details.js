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

// Hides next-violations in building_details
$("#next-violations").hide();


// Selects from write-a-review button in building_details.html
// and send to write_review.html page
$("#write-a-review").on("click"), () => {
    window.location.replace("/write_review")
};

// $.get("/violations_by_class.json", (res) => {
//   console.log(res);
// });

console.log($("#violation-class").data("chart"))

// Chart.js test
const testChart = new Chart(
    $('#violation-class'),
    {
    type: 'bar',
    data:($("#violation-class").data("chart"))
    }
);