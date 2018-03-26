$(document).ready(function () {
    // button effects and animations
    $(".vote").hover(function () {
        $(this).animate({height: 64, width: 64}, 100);
    }, function () {
        $(this).animate({height: 48, width: 48}, 100);
    });
    $(".down-vote").hover(function () {
        $(this).animate({height: 64, width: 64}, 100);
    }, function () {
        $(this).animate({height: 48, width: 48}, 100);
    });
    $(".video-add").hover(function () {
        $(this).css({"background-color": "gold", "color": "black"});
    }, function () {
        $(this).css({"background-color": "blue", "color": 'white'});

    });

    $(".video-remove").hover(function () {
        $(this).css({"background-color": "red", "color": "black"});
    }, function () {
        $(this).css({"background-color": "blue", "color": 'white'});

    });
    $(".joke-remove").hover(function () {
        $(this).css({"background-color": "red", "color": "black"});
    }, function () {
        $(this).css({"background-color": "blue", "color": 'white'});

    });
    $('.flag').hover(function() {
        $(this).animate({height: 32, width: 32},50);
    }, function(){
        $(this).animate({height: 30, width:30},50);
    });
    // emoji-picker initializer
    $(function () {
        // Initializes and creates emoji set from sprite sheet
        window.emojiPicker = new EmojiPicker({
            emojiable_selector: '[data-emojiable=true]',
            assetsPath: '/static/lib/img/',
            popupButtonClasses: 'fa fa-smile-o'
        });
        // Finds all elements with `emojiable_selector` and converts them to rich emoji input fields
        // You may want to delay this step if you have dynamically created input fields that appear later in the loading process
        // It can be called as many times as necessary; previously converted input fields will not be converted again
        window.emojiPicker.discover();
    });


});

