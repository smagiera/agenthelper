function update() {
  var date1 = document.getElementById("from").value;
  var date2 = document.getElementById("to").value;
  $('#results').load("policies/"+date1+"&"+date2+" #result", function() {
    var table = $('#policy_list').DataTable();
    new $.fn.dataTable.Buttons(table, {
buttons: [
    'excel', 'pdf'
]
});
table.buttons(0, null).containers().appendTo('#result');
  });
  
    
}