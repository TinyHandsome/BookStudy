// 清除所有框中的内容
$(function () {
    $("#clear_button").click(function () {
        $("#my_cookie").val("");
        $("#defjson").val("");
        alert_green("清空成功");
    })
})
