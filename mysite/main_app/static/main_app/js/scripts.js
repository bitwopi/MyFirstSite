document.getElementById('login').addEventListener('click', 
function(){
    document.querySelector('.bg-modal').style.display = 'flex';
});
document.querySelector('.close').addEventListener('click', 
function(){
    document.querySelector('.bg-modal').style.display = "none";
});
document.getElementById('sign-up').addEventListener('click',
function(){
    document.querySelector('.bg-modal-register').style.display = 'flex';
    document.querySelector('.bg-modal').style.display = "none";
});
document.getElementById('close-reg').addEventListener('click',
function(){
    document.querySelector('.bg-modal-register').style.display = 'none';
});