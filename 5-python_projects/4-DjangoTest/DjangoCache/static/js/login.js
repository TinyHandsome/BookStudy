$(function () {
    $("img").click(function () {
        console.log("点到我了");
        $(this).attr("src", "/app/getcode/?t=" + Math.random());
    })
})