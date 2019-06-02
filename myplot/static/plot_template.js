$(function(){
  console.log(getUrlVars())
})

function getUrlVars() {
  var vars = []
  var url = window.location.search;
  hash  = url.slice(1).split('&');
  for (var i = 0; i < hash.length; i++) {
    array = hash[i].split('=');
    vars.push(array[0]);
    vars[array[0]] = array[1];
  }
  return vars;
}
function plotUserData() {
// Buid query parameter
  console.log();
    var param = {};
    var vals = getUrlVars();
    // param["start"] = document.getElementById("start").value;
    // param["end"] = document.getElementById("end").value;
    param["file_name"] = vals["file_name"]
    console.log(vals["file_name"]);
    var query = jQuery.param(param);



// Query with a new parameter
    $.get("/plot/data" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};
//
// Register Event handler
//

document.getElementById("plot").addEventListener("click", function(){
    plotUserData();
}, false);
// plotbtc();
