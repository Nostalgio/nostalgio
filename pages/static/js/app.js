$(document).foundation();

$(document).ready(function(){

    $('.bxslider').bxSlider();

    $(document).ready(function() {
        $('#faq .block-faq_question').click(function() {
            $(this).next('.block-faq_answer').slideToggle(500);
            $(this).toggleClass('close');
        });
    });

    $('.reveal_modal').click(function(event) {
        event.preventDefault();

        $('#modal-content').empty();
        var link = $(this).attr("href");
        $('#modal-content').load(link + " .modal-content");
    });

    $('.testimonials').bxSlider({
        auto: true,
        mode: 'vertical',
        pager: false,
        controls: false,
        slideMargin:3,
    });

    $('.adverts').bxSlider({
        minSlides: 3,
        maxSlides: 3,
        slideWidth: 210,
        slideMargin: 15
    });


    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('.scrollup').fadeIn();
        } else {
            $('.scrollup').fadeOut();
        }
    });

    $('.scrollup').click(function() {
        $("html, body").animate({
            scrollTop: 0
        }, 600);
        return false;
    });

    $('.scrolldown').click(function() {
        $("html, body").animate({
            scrollTop: ($(window).innerHeight() - 40)
        }, 600);
        return false;
    });

    var center_divs = function center_divs() {
        var MENU_HEIGHT = 54,
            FUDGE = 10,
            MOBILE_WIDTH = 640,
            divHeight = $('.vertical-center').innerHeight(),
            windowHeight = $(window).innerHeight(),
            windowWidth = $(window).innerWidth();
        if (windowWidth < MOBILE_WIDTH) {
            $('.intro').stop().removeAttr('style');
            $('.vertical-center').stop().removeAttr('style');
        } else if ((windowHeight - MENU_HEIGHT) < divHeight) {
            $('.intro').css({ 'height': 'auto'});
        } else if (windowWidth > MOBILE_WIDTH) {
            $('.intro').css({ 'height': '100vh'});
            // Vertically align
            $('.vertical-center').animate({
                'margin-top': (windowHeight/2 - divHeight/2 + FUDGE)
            });
        }
    };

    center_divs();
    $(window).on('resize', function() {
        center_divs();
    });
});

