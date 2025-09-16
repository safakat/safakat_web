// Load Top Bar
fetch('topbar.html')
  .then(response => response.text())
  .then(data => {
    document.getElementById('topbar-container').innerHTML = data;

    // Mobile menu toggle after loading top bar
    document.querySelector(".hamburger").addEventListener("click", () => {
      document.querySelector(".nav-links").classList.toggle("active");
    });
  });

// Typing Animation
document.addEventListener("DOMContentLoaded", function() {
    const roles = ["Python Developer.", "Data Analyst."];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    const typingSpeed = 100; // ms per character
    const deletingSpeed = 60; 
    const delayBetweenRoles = 800; // pause before deleting
    const roleElement = document.getElementById("role");

    function typeRole() {
        const currentRole = roles[roleIndex];
        
        if (isDeleting) {
            roleElement.textContent = currentRole.substring(0, charIndex--);
        } else {
            roleElement.textContent = currentRole.substring(0, charIndex++);
        }

        if (!isDeleting && charIndex === currentRole.length) {
            setTimeout(() => isDeleting = true, delayBetweenRoles);
        } else if (isDeleting && charIndex < 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
        }

        const timeout = isDeleting ? deletingSpeed : typingSpeed;
        setTimeout(typeRole, timeout);
    }

    typeRole();
});


