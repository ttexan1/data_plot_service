$(function(){
  listOfCsv()
})

function listOfCsv(){
  $.get("/files/index", function(data) {
    var list = document.getElementById("csv_list");
    for (var i=0; i < data.result.length;  i++){
      var li = document.createElement('li');
      var ref = document.createElement('a');
      ref.setAttribute('href', '/plot/free?file_name='+ data.result[i])
      ref.textContent = data.result[i]
      li.appendChild(ref);
      list.appendChild(li);
    }
  });
}
