document.addEventListener("DOMContentLoaded", function() {
    const navPlaceholder = document.getElementById("navbar-placeholder");
    const navPath = navPlaceholder.getAttribute("data-nav-path") || "includes/nav.html";
    fetch(navPath)
        .then(response => response.text())
        .then(data => {
            navPlaceholder.innerHTML = data;
            var path = window.location.pathname;
            var page = path.split("/").pop();
            if (page === "") {
                page = "index.html";
            }
            var navLinks = document.querySelectorAll(".navbar-nav .nav-link");
            navLinks.forEach(function(link) {
                if (link.getAttribute("href") === page) {
                    link.classList.add("active");
                }
            });
        });
});