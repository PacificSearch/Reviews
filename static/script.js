function toggleFilters() {
  var panel = document.getElementById("filterPanel");
  if (!panel) return; // Agar element nahi milta, to function exit kare

  // Compute current display value from CSS
  var computedDisplay = window.getComputedStyle(panel).display;
  if (computedDisplay === "none") {
    panel.style.display = "block";
  } else {
    panel.style.display = "none";
  }
}

function toggleSubOptions(id) {
  var sub = document.getElementById(id);
  if (!sub) return; // Agar element nahi milta, to function exit kare

  // Compute current display value from CSS
  var computedDisplay = window.getComputedStyle(sub).display;
  if (computedDisplay === "none") {
    sub.style.display = "block";
  } else {
    sub.style.display = "none";
  }
}
