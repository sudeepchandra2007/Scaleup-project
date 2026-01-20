document.addEventListener("DOMContentLoaded", () => {
    const options = document.querySelectorAll(".option");
    
    // Animate the options on load
    options.forEach((option, index) => {
        option.style.animationDelay = `${index * 0.1}s`;
    });

    options.forEach(option => {
        option.addEventListener("mouseenter", () => {
            option.style.transform = "scale(1.1)";
        });

        option.addEventListener("mouseleave", () => {
            option.style.transform = "scale(1)";
        });
    });
});
