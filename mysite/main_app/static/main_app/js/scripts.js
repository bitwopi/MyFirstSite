// Burger menu
const iconMenu = document.querySelector('.menu-icon');
if(iconMenu){
    const navLinks = document.querySelector('.nav-links');
    iconMenu.addEventListener("click", function(e){
        document.body.classList.toggle('lock');
        iconMenu.classList.toggle('active');
        navLinks.classList.toggle('active');
    });
}