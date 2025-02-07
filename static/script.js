
// Toggle the Filter Panel display
function toggleFilters() {
  const panel = document.getElementById('filterPanel');
  panel.style.display = (panel.style.display === 'block') ? 'none' : 'block';
}

// Toggle the display of sub-options for a given category
function toggleSubOptions(categoryId) {
  const options = document.getElementById(categoryId);
  options.style.display = (options.style.display === 'block') ? 'none' : 'block';
}

// Language Switcher Functionality
document.querySelectorAll('.lang-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    document.querySelector('.lang-btn.active').classList.remove('active');
    this.classList.add('active');
  });
});

// Close filter panel when clicking outside
document.addEventListener('click', function(e) {
  if (!e.target.closest('.filter-toggle') && !e.target.closest('.filter-panel')) {
    document.getElementById('filterPanel').style.display = 'none';
  }
});

