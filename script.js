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

// Toggle function for filter options
function toggleFilterOptions() {
  const filterOptions = document.getElementById('filterOptions');
  if (filterOptions.style.display === "block") {
    filterOptions.style.display = "none";
  } else {
    filterOptions.style.display = "block";
  }
}

// Language Switcher functionality
const englishBtn = document.getElementById('english-btn');
const hinglishBtn = document.getElementById('hinglish-btn');

if (englishBtn && hinglishBtn) {
  englishBtn.addEventListener('click', function() {
    englishBtn.classList.add('active');
    hinglishBtn.classList.remove('active');
    alert("Switched to English");
  });

  hinglishBtn.addEventListener('click', function() {
    hinglishBtn.classList.add('active');
    englishBtn.classList.remove('active');
    alert("Switched to Hinglish");
  });
} else {
  console.error("Language buttons not found");
}
