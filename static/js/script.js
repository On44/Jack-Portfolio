// Smooth scrolling for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});

// Toggle Navbar for Mobile View
const navbarToggle = document.getElementById('navbar-toggle');
const navbarMenu = document.getElementById('navbar-menu');

// Check if navbar toggle and menu exist in DOM
if (navbarToggle && navbarMenu) {
    navbarToggle.addEventListener('click', () => {
        navbarMenu.classList.toggle('active');
    });
}

// Dynamic Year in Footer
const footerYear = document.getElementById('footer-year');
if (footerYear) {
    footerYear.textContent = new Date().getFullYear();
}

// Example of an animation trigger (fade-in effect for projects)
const projectCards = document.querySelectorAll('.project-card');
const fadeInObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
            observer.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.5
});

projectCards.forEach(card => {
    fadeInObserver.observe(card);
});
