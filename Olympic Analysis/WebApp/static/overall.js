// Graph Plot



X = document.getElementById("X").innerText;
Y = document.getElementById("Y").innerText;
var xValues = X.split(" ");
var yValues = Y.split(" ");

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [
      {
        fill: false,
        lineTension: 0,
        backgroundColor: "rgba(0,0,255,1.0)",
        borderColor: "rgba(0,0,255,0.1)",
        data: yValues,
      },
    ],
  },
  options: {
    legend: { display: false },

    scales: {
      yAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: "No of Countrys",
          },
        },
      ],
      xAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: "Years",
          },
        },
      ],
    },
  },
});

// Event Over Years
X1 = document.getElementById("X1").innerText;
Y1= document.getElementById("Y1").innerText;
var xValues1 = X1.split(" ");
var yValues1 = Y1.split(" ");

new Chart("myChart1", {
  type: "line",
  data: {
    labels: xValues1,
    datasets: [
      {
        fill: false,
        lineTension: 0,
        backgroundColor: "rgba(0,0,255,1.0)",
        borderColor: "rgba(0,0,255,0.1)",
        data: yValues1,
      },
    ],
  },
  options: {
    legend: { display: false },

    scales: {
      yAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: "No of Event",
          },
        },
      ],
      xAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: "Years",
          },
        },
      ],
    },
  },
});


// Athletes Over the Years
X2 = document.getElementById("X2").innerText;
Y2 = document.getElementById("Y2").innerText;
var xValues2 = X2.split(" ");
var yValues2 = Y2.split(" ");

new Chart("myChart2", {
  type: "line",
  data: {
    labels: xValues2,
    datasets: [
      {
        fill: false,
        lineTension: 0,
        backgroundColor: "rgba(0,0,255,1.0)",
        borderColor: "rgba(0,0,255,0.1)",
        data: yValues2,
      },
    ],
  },
  options: {
    legend: { display: false },

    scales: {
      yAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: "No of Athletes",
          },
        },
      ],
      xAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: "Years",
          },
        },
      ],
    },
  },
});


