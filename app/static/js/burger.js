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

//     var heroHeight,headerHeight,windowHeight;

//     $(window).on('resize',function(){
//         headerHeight = $('.header-main').height();
//         windowHeight = $(window).height();
//         heroHeight = windowHeight - headerHeight
//         $('.hero-home').css('height',heroHeight)
//         console.log(heroHeight)
//     })


// })

$(window).scroll(function() {
    if ($(window).scrollTop() > 10) {
        $('.header-main').css('box-shadow','0px 1px 10px #999');
    } else {
        $('.header-main').css('box-shadow','none');
    }
});