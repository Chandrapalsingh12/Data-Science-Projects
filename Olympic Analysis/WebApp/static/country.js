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



//                                      COUNTRY

//Medal Taily of Country 
c_year = document.getElementById("c_year").innerText;
c_medal = document.getElementById("c_medal").innerText;
var c1 = c_year.split(" ");
var c2 = c_medal.split(" ");

new Chart("country_medal", {
  type: "line",
  data: {
    labels: c1,
    datasets: [
      {
        fill: false,
        lineTension: 0,
        backgroundColor: "rgba(0,0,255,1.0)",
        borderColor: "rgba(0,0,255,0.1)",
        data: c2,
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
            labelString: "Medals",
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