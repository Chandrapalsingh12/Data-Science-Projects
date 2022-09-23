function checkedOnClick(el) {
  // Select all checkboxes by class
  var checkboxesList = document.getElementsByClassName("checkoption");
  for (var i = 0; i < checkboxesList.length; i++) {
    checkboxesList.item(i).checked = false; // Uncheck all checkboxes
  }

  el.checked = true; // Checked clicked checkbox
}

function myFunction() {
  var x = document.getElementById("centered_nav");
  if (x.className === "rc_nav") {
    x.className += " responsive";
  } else {
    x.className = "rc_nav";
  }
}

const darkMode = document.getElementById('checkbox');

darkMode.addEventListener('change', () => {
	document.body.classList.toggle('dark');
});






x1 = document.getElementById("x1").innerText;
x2 = document.getElementById("x2").innerText;
x3 = document.getElementById("x3").innerText;
x4 = document.getElementById("x4").innerText;

var c1 = x1.split(" ");
var c2 = x2.split(" ");
var c3 = x3.split(" ");
var c4 = x4.split(" ");

var speedCanvas = document.getElementById("athlete");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var dataFirst = {
  label: "Age",
  data: c1,
  lineTension: 0,
  fill: false,
  borderColor: "red",
};

var dataSecond = {
  label: "Gold",
  data: c2,
  lineTension: 0,
  fill: false,
  borderColor: "blue",
};

var datathird = {
  label: "Silver",
  data: c3,
  lineTension: 0,
  fill: false,
  borderColor: "green",
};
var dataFourth = {
  label: "Bronze",
  data: c4,
  lineTension: 0,
  fill: false,
  borderColor: "orange",
};

var speedData = {
  labels: ["20yr","30yr","40yr","50yr","60yr","70yr","80yr","90yr"],
  datasets: [dataFirst, dataSecond, datathird, dataFourth],
};

var chartOptions = {
  legend: {
    display: true,
    position: "top",
    labels: {
      boxWidth: 80,
      fontColor: "black",
    },
  },
};

var lineChart = new Chart(speedCanvas, {
  type: "line",
  data: speedData,
  options: chartOptions,
});



// Gender



Y = document.getElementById("Y").innerText;
X1 = document.getElementById("X1").innerText;
X2 = document.getElementById("X2").innerText;

var total = Y.split(" ");
var X11 = X1.split(" ");
var X22 = X2.split(" ");

var speedCanvas = document.getElementById("Gender");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var dataFirst = {
  label: "Male",
  data: X11,
  lineTension: 0,
  fill: false,
  borderColor: "red",
};

var dataSecond = {
  label: "Female",
  data: X22,
  lineTension: 0,
  fill: false,
  borderColor: "blue",
};

var speedData = {
  labels: total,
  datasets: [dataFirst, dataSecond],
};

var chartOptions = {
  legend: {
    display: true,
    position: "top",
    labels: {
      boxWidth: 80,
      fontColor: "black",
    },
  },
};

var lineChart = new Chart(speedCanvas, {
  type: "line",
  data: speedData,
  options: chartOptions,
});












