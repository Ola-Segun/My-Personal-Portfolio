var sections = document.querySelectorAll('section');
var body = document.querySelector('body');
var navLi = document.querySelectorAll('body nav .navCon ul li')
var dot = document.querySelectorAll('li.dot')


window.addEventListener('scroll', ()=> {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight; 

        if(pageYOffset >= (sectionTop - sectionHeight / 3)){
            current = section.getAttribute('id');
            console.log(current);
        }
    })
    navLi.forEach( li => {
        li.classList.remove('active');
        if(li.classList.contains(current)){
            li.classList.add('active');
        }
    })
    dot.forEach( item => {
        item.classList.remove('activeDot');
        if(item.classList.contains(current)){
            item.classList.add('activeDot');
        }
    })
})



var menuToggle = document.querySelector('.menuToggle');
var nav = document.querySelector('nav');


menuToggle.onclick = function(){
    nav.classList.toggle('open')
}

// MODAL DISPLAY

var login_show = document.getElementById('login-show');
var login_modal = document.getElementById('login-modal');
var close_modal = document.getElementById('close-modal');

login_show.onclick = function(){
    login_modal.classList.remove('hidden')
}
close_modal.onclick = function(){
    login_modal.classList.add('hidden')
}

// window.addEventListener('load', function() {
//     var bodyWidth = document.body.clientWidth;
//     var navHeight = 0;
//     if (bodyWidth < 650) {
//         body.classList.add('mobile');
//         body.classList.remove('desktop')
//         }
//     }
// );
