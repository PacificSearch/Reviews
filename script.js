// Ensure the DOM content is fully loaded before running JS code
document.addEventListener("DOMContentLoaded", function() {
  // Language switch functionality: find all buttons with class 'lang-btn'
  var langButtons = document.querySelectorAll('.lang-btn');
  
  langButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      // Remove 'active' class from all language buttons
      langButtons.forEach(function(btn) {
        btn.classList.remove('active');
      });
      // Add 'active' class to the clicked button
      this.classList.add('active');
      // Optionally, perform any further action based on the selected language
      console.log("Language switched to:", this.textContent);
    });
  });
  
  // (Optional) If you already have filter toggle functions in this file, include them as well:
  window.toggleFilters = function() {
    var panel = document.getElementById("filterPanel");
    if (panel) {
      var currentDisplay = window.getComputedStyle(panel).display;
      panel.style.display = (currentDisplay === "none") ? "block" : "none";
    }
  };

  window.toggleSubOptions = function(id) {
    var sub = document.getElementById(id);
    if (sub) {
      var currentDisplay = window.getComputedStyle(sub).display;
      sub.style.display = (currentDisplay === "none") ? "block" : "none";
    }
  };
});
