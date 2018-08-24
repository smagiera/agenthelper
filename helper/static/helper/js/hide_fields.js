function Hide() {
    if(document.getElementById('id_policy_type').options[document.getElementById('id_policy_type').selectedIndex].value == "1") {
         document.getElementById('id_property').style.display = 'none';
         $('label[for="id_property"]').hide();
         $("select[name='vehicle']").parent().css("display", '');
         $('label[for="id_vehicle"]').show();
    } else {
         document.getElementById('id_property').style.display = '';
         $('label[for="id_property"]').show();
         $("select[name='vehicle']").parent().css("display", 'none');
         $('label[for="id_vehicle"]').hide();
    }
}

window.onload = function() {
    document.getElementById('id_policy_type').onchange = Hide;
};
Hide();