$('#main-slide').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    items: 1

})

$('#bank').owlCarousel({
    items: 4,
    responsive: {
        0: {
            items: 1,
            loop: true,
        },
        768: {
            items: 3,
            loop: true,
        },
        1200: {
            items: 4,
            loop: true,
        },
    },
    nav: true,
    loop: true,
    autoplay: true,
    autoplayTimeout: 5000,
    autoplayHoverPause: true,
    margin: 10,
})


var rule = $('#rule')[0].children;

for (var i = 0; i < rule.length; i++) {

    var h2 = rule[i].children[0];
    var div = rule[i].children[1];
    $(h2).on('click', function () {
        $(this).siblings().slideToggle()
    })
}


var btnmenu = $('#btn-menu')[0].children;
var open = false
$('#btn-menu').on('click', function () {
    open = !open

    btnmenu[0].style.transform = open ? 'rotate(45deg)' : 'rotate(0)';
    btnmenu[1].style.transform = open ? 'translateX(10px)' : 'translateX(0)';
    btnmenu[1].style.opacity = open ? '0' : '1';
    btnmenu[2].style.transform = open ? 'rotate(-45deg)' : 'rotate(0)';
    $('#menu').css({
        'transform': open ? 'translateX(-100%)' : 'translateX(0)',
    })
    $(this).css({
        'position': open ? 'fixed' : 'absolute',
    });
})

$('.colse-modal').on('click', function () {
    $('body').find('.bg-black').css({ 'display': 'none' })
})


function OpenSignUp() {
    $('#signup-modal').css({ 'display': 'block' })
}

function OpenLogin() {
    $('#login-modal').css({ 'display': 'block' })
}


var contactItem = $('#contact-wrapp').children()


for (let i = 0; i <= contactItem.length; i++) {
    $(contactItem[i]).on('mouseover', function () {
        $(this).css({ 'transform': 'translate(0, -50%)' });
    })
    $(contactItem[i]).on('mouseout', function () {
        $(this).css({ 'transform': 'translate(180px, -50%)' });
    })

}