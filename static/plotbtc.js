//
// Calculator
//
function plotbtc() {
// Buid query parameter
    var param = {};
    param["start"] = document.getElementById("start").value;
    param["end"] = document.getElementById("end").value;
    var query = jQuery.param(param);

// Query with a new parameter
    $.get("/plot/btc" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};

function plotLivingCost() {
// Buid query parameter
    // var param = {};
    // param["start"] = document.getElementById("start").value;
    // param["end"] = document.getElementById("end").value;
    // var query = jQuery.param(param);
    var query = "l=10"
// Query with a new parameter
    $.get("/living_cost" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};
//
// Register Event handler
//


document.getElementById("myplot").addEventListener("click", function(){
    plotLivingCost();
}, false);
// document.getElementById("plot").addEventListener("click", function(){
//     plotbtc();
// }, false);
// plotbtc();
