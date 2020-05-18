// jQuery(function ($) {

//     $('.header-nav-wrapper').on('click', function () {
//         $('.overlay').toggle();

//         setTimeout(function () {
//             $('.overlay').addClass('is-open')
//         }, 200)

//         $('.body').addClass('overflow')
//         $('.nav-responsive').addClass('nav-transition')
//         $('.header-nav-burger').addClass('is-animate')
//     })

//     $('.overlay').on('click', function () {

//         setTimeout(function () {
//             $('.overlay').removeClass('is-open')
//             $('.overlay').toggle();
//         }, 500)

//         $('.body').removeClass('overflow')
//         $('.nav-responsive').removeClass('nav-transition')
//         $('.header-nav-burger').removeClass('is-animate')
//     })
// })

// $(window).scroll(function() {
//     if ($(window).scrollTop() > 10) {
//         $('.header-main').css('box-shadow','0px 1px 10px #999');
//     } else {
//         $('.header-main').css('box-shadow','none');
//     }
// });


var headerHeight;
var screenHeight;
function resize() {
    screenHeight = $(window).innerHeight();
    headerHeight = $('.header-main').innerHeight();
    valueForm = screenHeight - headerHeight;
    if ($('.wrapper').innerHeight() < valueForm) {
        $('.wrapper').css('height', valueForm);
    }else{
        $('.wrapper').css('height', 'auto');
    }
    
}

resize();
$(window).resize(resize);