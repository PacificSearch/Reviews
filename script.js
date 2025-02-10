document.addEventListener("DOMContentLoaded", function() {
  // Language switch functionality:
  var langButtons = document.querySelectorAll('.lang-btn');
  langButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      langButtons.forEach(function(btn) {
        btn.classList.remove('active');
      });
      this.classList.add('active');
      console.log("Language switched to:", this.textContent);
    });
  });
  
  // Filter toggle functionality:
  window.toggleFilters = function() {
    var panel = document.getElementById("filterPanel");
    if (!panel) return;
    var currentDisplay = window.getComputedStyle(panel).display;
    panel.style.display = (currentDisplay === "none") ? "block" : "none";
  };

  // Toggle sub-options (if needed)
  window.toggleSubOptions = function(id) {
    var sub = document.getElementById(id);
    if (!sub) return;
    var currentDisplay = window.getComputedStyle(sub).display;
    sub.style.display = (currentDisplay === "none") ? "block" : "none";
  };
});
