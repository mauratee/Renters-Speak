"use strict";

alert("JS is connected");

// Enable reviews tab
var triggerTabList = [].slice.call(document.querySelectorAll('#nav-reviews-tab'))
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl)

  triggerEl.addEventListener('click', function (event) {
    event.preventDefault()
    tabTrigger.show()
  })
})

// Enable landlord tab
var triggerTabList = [].slice.call(document.querySelectorAll('#nav-landlord-tab'))
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl)

  triggerEl.addEventListener('click', function (event) {
    event.preventDefault()
    tabTrigger.show()
  })
})

// Enable violations tab
var triggerTabList = [].slice.call(document.querySelectorAll('#nav-violations-tab'))
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl)

  triggerEl.addEventListener('click', function (event) {
    event.preventDefault()
    tabTrigger.show()
  })
})



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
    // Alert appears for a short time and then slowly fades out
    $("#violation-alert").show().delay(1000).fadeOut(2000);
  }
});

// Hides violations a few at a time
$("#show-fewer-violations").on("click", function (evt) {
  evt.preventDefault();
  $(".violation-list:visible").slice(0,4).slideUp();
  // If all violations hidden, flash alert
  if ($(".violation-list:visible").length == 0) {
    // Alert appears for a short time and then slowly fades out
    $("#end-of-list").show().delay(1000).fadeOut(2000);
  }
})

// Shows all remaining hidden violations
$("#show-all-violations").on("click", function (evt) {
  // console.log("we clicked show all violations");
  evt.preventDefault();
  if ($(".violation-list:hidden").length != 0) {
    $(".violation-list:hidden").slideDown();
    $("#show-all-violations").text("Hide All Violations")
  }
  else {
    $(".violation-list:visible").slideUp();
    $("#show-all-violations").text("Show All Violations")
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
  $(".violations-class-info-trigger")
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

console.log($("#violation-date").data("chart"))

Chart.defaults.elements.arc.backgroundColor = ["#5E309c", "#56b1e7", "#5F19e6"]  ;

// construct Chart.js doughnut graph for violation classes
const testChart = new Chart(
    $('#violation-class'),
    {
    type: 'doughnut',
    data:($("#violation-class").data("chart")),
    options: {
      plugins: {
        legend: {
          labels: {
              font: {
                family: "monospace"
              },
          }
        },
          title: {
              display: true,
              text: 'Violations by Class',
              font: {
                family: "monospace"
              },
              padding: {
                  top: 15,
                  bottom: 5
              }
          }
      }
  }
    }
);

// construct Chart.js doughnut graph for violation classes
const barChart = new Chart(
  $('#violation-date'),
  {
  type: 'bar',
  data:($("#violation-date").data("chart")),
  options: {
    plugins: {
        legend: {
          display: false,
        },
        title: {
            display: true,
            text: 'Violations by Year',
            font: {
              family: "monospace"
            },
            padding: {
                top: 15,
                bottom: 5
            }
        }
    }
}
  }
);