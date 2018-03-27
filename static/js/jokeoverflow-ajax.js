// add video from search results
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
// for up voting
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

// for down voting
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
// Adds a comment and updates comments
$(".com").submit(function (event) {
    event.preventDefault();
    var joke = $(this).attr('data-fjoke');
    var element = document.getElementById("com" + joke);
    var text = element.value;
    $.get('/jokeoverflow/add_comment/', {joke: joke, text: text}, function (data) {
        $('#comment-container' + joke).append(data).scrollTop(outerHeight*10000);// Should work for a while to scroll to the most recently added comment
        $('.emoji-wysiwyg-editor').html('');  // clears the textbox

    });


});
// removes a video from database and updates profile page
$(".video-remove").click(function (data) {
    var video = $(this).attr('data-video');
    console.log(video);
    $.get('/jokeoverflow/video_remove/', {video: video}, function (data) {
        $('#videotable').html(data);
    });

});
// removes a joke from database and updates profile page
$(".joke-remove").click(function (data) {
    var joke = $(this).attr('data-joke');
    console.log(joke);
    $.get('/jokeoverflow/joke_remove/', {djoke: joke}, function (data) {
        $('#joketable').html(data);


    });

});

$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        console.log(this);
        $.get('/jokeoverflow/suggest_joke/', {suggestion: query}, function(data){
         $('#jokeslist').html(data);
        });
});
// flags joke
$(".flag").click(function (data) {
    var joke = $(this).attr('data-fjoke');
    console.log(joke);
    $.get('/jokeoverflow/flag/', {fjoke: joke}, function (data) {
        $('#resp' + joke).html(data);
        setTimeout(function () {
            $('#resp' + joke).html('')
        }, 750);
    });
});


