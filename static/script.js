function toggleFilters() {
    var panel = document.getElementById("filterPanel");
    if (panel.style.display === "block") {
        panel.style.display = "none";
    } else {
        panel.style.display = "block";
    }
}

function toggleSubOptions(id) {
    var sub = document.getElementById(id);
    if (sub.style.display === "block") {
        sub.style.display = "none";
    } else {
        sub.style.display = "block";
    }
}
