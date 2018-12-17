function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

async function setup() {
    await sleep(100);
    console.log('setup start');
    start = $( "#id_date_start" );
    end = $( "#id_date_end" );
    issued = $( "#id_date_issued" );
    d = new Date();
    d = d.setFullYear(d.getFullYear() + 1);
    d = new Date(d).setDate(new Date(d).getDate()-1);
    end_date = d;
    start.datepicker('setDate', new Date());
    end.datepicker('setDate', new Date(end_date));
    issued.datepicker('setDate', new Date());
}