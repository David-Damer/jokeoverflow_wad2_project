$(document).ready(function () {
    $(".vote").hover(function () {
        $(this).animate({height: 56, width: 56}, 100);
    }, function () {
        $(this).animate({height: 48, width: 48}, 100);
    });
    $(".down-vote").hover(function () {
        $(this).animate({height: 56, width: 56}, 100);
    }, function () {
        $(this).animate({height: 48, width: 48}, 100);
    });
    $(".video-add").hover(function () {
        $(this).css({"background-color": "gold", "color": "black"});
    }, function () {
        $(this).css({"background-color": "blue", "color": 'white'});
    });

});

