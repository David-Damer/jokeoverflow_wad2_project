$('.video-add ').click(function () {
    var id = $(this).attr("data-id");
    var url = $(this).attr("data-url");
    var code = $(this).attr("data-code");
    var thumb = $(this).attr("data-thumb");
    var title = $(this).attr("data-title");
    var me = $(this);
    $.get('/jokeoverflow/add/',
        {vid_id: id, url: url, code: code, thumb: thumb, title: title}, function (data){
        $('#videos').html(data);
            me.hide();

        });
});
$(".vote").click(function () {
    var joke = $(this).attr('data-joke');
    console.log(this);
    $.get('/jokeoverflow/upvote/', {djoke: joke}, function (data) {
        $('#u' + joke).html(data);
    });

});
$(".down-vote").click(function () {
    var joke = $(this).attr('data-joke');
    console.log(this);
    $.get('/jokeoverflow/downvote/', {djoke: joke}, function (data) {
        $('#d' + joke).html(data);
    });

});