/**
 * Toggles the display of sub-options for a filter category.
 * @param {HTMLElement} element - The header element clicked.
 */
function toggleSubOptions(element) {
  const subOptions = element.nextElementSibling;
  subOptions.style.display = subOptions.style.display === "block" ? "none" : "block";
}

// Language Switcher Functionality
const englishBtn = document.getElementById('englishBtn');
const hinglishBtn = document.getElementById('hinglishBtn');

englishBtn.addEventListener('click', () => {
  englishBtn.classList.add('active');
  hinglishBtn.classList.remove('active');
  // Implement language switching logic here
  console.log("Switched to English");
});

hinglishBtn.addEventListener('click', () => {
  hinglishBtn.classList.add('active');
  englishBtn.classList.remove('active');
  // Implement language switching logic here
  console.log("Switched to Hinglish");
});
