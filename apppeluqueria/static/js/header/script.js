const toggler = document.querySelector('.menu_toggler');
const menu = document.querySelector('.menu');
const grid = document.querySelector('.grid-container-header');
const bgmenu = document.querySelector('.bgmenu');
/* BOTONES MENU + EFFECT */
toggler.addEventListener('click', () => {
    toggler.classList.toggle('active');
    menu.classList.toggle('active');
    grid.classList.toggle('open-w');
    bgmenu.classList.toggle('active');
})
bgmenu.addEventListener('click', () => {
    if (toggler.classList.contains('active')) {
        toggler.classList.toggle('active');
        menu.classList.toggle('active');
        grid.classList.toggle('open-w');
        bgmenu.classList.toggle('active');
    }
})


/* BOTONES LOGIN REGISTER Y RECOVER */
const boton_registrarse = document.querySelector('.regist');
const form_register = document.querySelector('.register');
const boton_login = document.querySelector('.logg');
const boton_login1 = document.querySelector('.logge');
const form_login = document.querySelector('.login');
const boton_recover = document.querySelector('.recov');
const boton_recover1 = document.querySelector('.recove');
const form_recover = document.querySelector('.recover');

boton_registrarse.addEventListener('click', () => {

    if (form_login.classList.contains('active')) {
        form_login.classList.toggle('active');
    }

    if (form_recover.classList.contains('active')) {
        form_recover.classList.toggle('active');
    }

    form_register.classList.toggle('active');
})

boton_login.addEventListener('click', () => {

    if (form_register.classList.contains('active')) {
        form_register.classList.toggle('active');
    }

    if (form_recover.classList.contains('active')) {
        form_recover.classList.toggle('active');
    }

    form_login.classList.toggle('active');

})

boton_login1.addEventListener('click', () => {

    if (form_register.classList.contains('active')) {
        form_register.classList.toggle('active');
    }

    if (form_recover.classList.contains('active')) {
        form_recover.classList.toggle('active');
    }

    form_login.classList.toggle('active');

})

boton_recover.addEventListener('click', () => {
    if (form_register.classList.contains('active')) {
        form_register.classList.toggle('active');
    }

    if (form_login.classList.contains('active')) {
        form_login.classList.toggle('active');
    }

    form_recover.classList.toggle('active');
})

boton_recover1.addEventListener('click', () => {
    if (form_register.classList.contains('active')) {
        form_register.classList.toggle('active');
    }

    if (form_login.classList.contains('active')) {
        form_login.classList.toggle('active');
    }

    form_recover.classList.toggle('active');
})


