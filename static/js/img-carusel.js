$(document).ready(function() {
    $('#owl-carousel-header').owlCarousel({
        loop: true,           //Включение зацикливания
        center: true,
        items: 1,             //количество элементов, отображаемых в карусели
        margin: 0,
        autoplay: true,
        autoplayTimeout: 5500,
        smartSpeed: 5000,
        animateIn: 'fadeIn',  //'linear',fadeIn
        animateOut: 'fadeOut',
        mouseDrag: false,    //Отключение передвижения мышью
        dots: true,          // навигация в виде точек
        //nav: true,
        margin: 0,
        center: true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    })
});


$(document).ready(function() {
    $('.owl-carousel-rooms').owlCarousel({
        loop: true,           //Включение зацикливания
        center: true,
        items: 1,             //количество элементов, отображаемых в карусели
        margin: 0,
        autoplay: false,
        autoplayTimeout: 3500,
        smartSpeed: 3000,
        animateIn: 'linear',  //'linear',fadeIn
        animateOut: 'fadeOut',
        mouseDrag: false,    //Отключение передвижения мышью
        dots: true,          // навигация в виде точек
        //nav: true,
        margin: 0,
        center: true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    })
});

