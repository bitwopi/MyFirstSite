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

// Profile dropdown
const dropdown = document.querySelector('.profile-dropdown');
const submenu = document.querySelector('.submenu');
const container = document.querySelector('.triangle-container')
if(dropdown){
    dropdown.addEventListener("mouseover", function(e){
        submenu.removeAttribute('hidden');
        container.classList.add('active');
        dropdown.classList.add('bordering');
    })
    submenu.addEventListener("mouseleave", function(e){
        submenu.setAttribute('hidden', '');
        container.classList.remove('active');
    })
}