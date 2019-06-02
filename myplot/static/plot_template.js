$(function(){
  makeForm()
})


function makeForm(){
  var param = {};
  var vals = getUrlVars();
  param["file_name"] = vals["file_name"]
  var query = jQuery.param(param);
  $.get("/plot/parameters" + "?" + query, function(data) {
    var form = document.getElementById("parameters");
    for (var i=0; i < data.result.length;  i++){
      var p = document.createElement('p')
      var input = document.createElement('input');
      input.setAttribute('name', data.result[i])
      input.setAttribute('value', "true")
      input.setAttribute('type', "checkbox")
      input.setAttribute('class', "parameters");
      p.textContent = data.result[i]
      p.appendChild(input)
      form.appendChild(p);
    }
  });
}

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
  var param = {};
  var vals = getUrlVars();
  params_html = document.getElementsByClassName("parameters");
  for (var i=0; i< params_html.length; i++) {
    if (params_html[i].checked == true){
      param[params_html[i].name] = params_html[i].value
    }
  }
  param["file_name"] = vals["file_name"]
  var query = jQuery.param(param);
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
