$(document).ready(function () {
    $('.thumbnail').hover(function () {
        $(this).animate({paddingLeft: '+=5px'}, 200);

    }, function () {
        $(this).animate({paddingLeft: '-=5px'}, 200);
    });
});

