function update(url="") {
  var date1 = document.getElementById("from").value;
  var date2 = document.getElementById("to").value;
  $('#results').load(url+"policies/"+date1+"&"+date2+" #result", function() {
    var table = $('#policy_list').DataTable({
      language: {
          url: 'https://cdn.datatables.net/plug-ins/1.10.19/i18n/Polish.json'
      }});
    new $.fn.dataTable.Buttons(table, {
buttons: [
    'excel', 'pdf'
]
});
table.buttons(0, null).containers().appendTo('#result');
  });
  
    
}