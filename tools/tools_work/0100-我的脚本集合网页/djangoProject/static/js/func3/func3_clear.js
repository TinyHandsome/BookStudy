// 清除所有框中的内容
$(function () {
    $("#clear_button").click(function () {
        $("#cookie").val("");
        $("#defjson").val("");
        document.getElementById("copy_result").innerHTML = "清空成功";
    })
})
