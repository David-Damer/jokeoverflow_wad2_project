$('.video-add ').click(function () {
    var id = $(this).attr("data-id");
    var url = $(this).attr("data-url");
    var code = $(this).attr("data-code");
    var thumb = $(this).attr("data-thumb");
    var title = $(this).attr("data-title");
    var me = $(this);
    $.get('/jokeoverflow/add/',
        {vid_id: id, url: url, code: code, thumb: thumb, title: title}, function (data) {
            $('#videos').html(data);
            me.hide();

        });
});
$(".vote").click(function () {
    var joke = $(this).attr('data-joke');
    console.log(this);
    $.get('/jokeoverflow/upvote/', {djoke: joke}, function (data) {
        var response = $(data);
        var votes = response[0]["upvotes"];
        var msg = response[0]["msg"];
        var box = $('#u' + joke);
        box.html(msg);
        setTimeout(function () {
            box.html(votes);
        }, 1000);
    });
});


$(".down-vote").click(function () {
    var joke = $(this).attr('data-joke');
    console.log(this);
    $.get('/jokeoverflow/downvote/', {djoke: joke}, function (data) {
        var response = $(data);
        var votes = response[0]["downvotes"];
        var msg = response[0]["msg"];
        var box = $('#d' + joke);
        box.html(msg);
        setTimeout(function () {
            box.html(votes);
        }, 1000);
    });

});

$(".com").submit(function (data) {
    var joke = $(this).attr('data-fjoke');
    var element = document.getElementById("com" + joke);
    var text = element.value;
    console.log(text);
    $.get('/jokeoverflow/add_comment/', {joke: joke, text: text}, function (data) {
        $('#res' + joke).html(data);

    });


});


