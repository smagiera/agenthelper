// Our labels along the x-axis
var months = [
  "Styczeń",
  "Luty",
  "Marzec",
  "Kwiecień",
  "Maj",
  "Czerwiec",
  "Lipiec",
  "Sierpień",
  "Wrzesień",
  "Październik",
  "Listopad",
  "Grudzień"
];

var insurers = [
  "Warta",
  "Hestia",
  "MTU",
  "PZU",
  "Generali",
  "Proama",
  "Link4",
  "Reso",
  "TUW TUW",
  "TUW TUZ",
  "Uniqa",
  "Interrisk",
  "AXA",
  "Allianz"
];
// For drawing the lines
var premium = [86, 114, 106, 106, 107, 111, 133, 221, 783, 2478, 3215, 4169];
var ppi = [
  1200,
  600,
  800,
  230,
  5420,
  4320,
  2154,
  894,
  659,
  100,
  200,
  450,
  300,
  499
];

var ctx = document.getElementById("premiumTotal");
var myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: months,
    datasets: [
      {
        data: premium,
        label: "Przypis",
        borderColor: "#3e95cd",
        fill: false
      }
    ]
  }
});

var ctx = document.getElementById("premiumPerInsurer");
var myChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: insurers,
    datasets: [
      {
        data: ppi,
        label: "Przypis",
        backgroundColor: [
          "#3e95cd",
          "#8e5ea2",
          "#3cba9f",
          "#e8c3b9",
          "#c45850",
          "#ffc125",
          "#667937",
          "#256645",
          "#113377",
          "#8b5a2b",
          "#cd8500",
          "#00a0b0",
          "#4f372d",
          "#4d5d53"
        ]
      }
    ]
  }
});
