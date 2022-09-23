
const darkMode = document.getElementById('checkbox');

darkMode.addEventListener('change', () => {
	document.body.classList.toggle('dark');
});







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

