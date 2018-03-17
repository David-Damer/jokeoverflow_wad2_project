$('.video-add ').click(function () {
    var id = $(this).attr("data-id");
    var url = $(this).attr("data-url");
    var code = $(this).attr("data-code");
    var thumb = $(this).attr("data-thumb");
    var title = $(this).attr("data-title");
    var me = $(this);
    $.get('/jokeoverflow/add/',
        {vid_id: id, url: url, code: code, thumb: thumb, title: title}, function(data){
        me.hide();
        $('#videos').innerHTML(data);

        });
});
$(".vote").click(function () {
    var joke = $(this).attr('data');
    $.get('/jokeoverflow/upvote/', {djoke: joke}, function(data){
        $('#upvotes').html(data);
    } );

});