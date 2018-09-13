$( function() {
  $.datepicker.setDefaults($.datepicker.regional['pl']);
    from = $( "#from" )
      .datepicker({
        dateFormat: "yy-mm-dd",
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        defaultDate: new Date(),
      })
      .on( "change", function() {
        to.datepicker( "option", "minDate", getDate( this ) );
        update();
      }),
    to = $( "#to" ).datepicker({
      dateFormat: "yy-mm-dd",
      defaultDate: "+1w",
      changeMonth: true,
      numberOfMonths: 1,
    })
    .on( "change", function() {
      from.datepicker( "option", "maxDate", getDate( this ) );
      update();
    });

  function getDate( element ) {
    var date;
    try {
      date = $.datepicker.parseDate( dateFormat, element.value );
    } catch( error ) {
      date = null;
    }

    return date;
  }
  const dateOffset = (24*60*60*1000) * 14; //14 days
  let date1 = new Date();
  date1.setTime(date1.getTime() - dateOffset);
  from.datepicker('setDate', date1);
  to.datepicker('setDate', new Date());

  update();
} );