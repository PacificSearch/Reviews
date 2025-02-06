// script.js

// Toggle function for sub-options
function toggleSubOptions(element) {
  const subOptions = element.nextElementSibling;
  if (subOptions.style.display === "block") {
    subOptions.style.display = "none";
  } else {
    subOptions.style.display = "block";
  }
}

// Language Switcher functionality
const englishBtn = document.getElementById('english-btn');
const hinglishBtn = document.getElementById('hinglish-btn');

if (englishBtn && hinglishBtn) {
  englishBtn.addEventListener('click', function() {
    englishBtn.classList.add('active');
    hinglishBtn.classList.remove('active');
    // Add further functionality to switch content language if required.
    alert("Switched to English");
  });

  hinglishBtn.addEventListener('click', function() {
    hinglishBtn.classList.add('active');
    englishBtn.classList.remove('active');
    // Add further functionality to switch content language if required.
    alert("Switched to Hinglish");
  });
} else {
  console.error("Language buttons not found");
}
