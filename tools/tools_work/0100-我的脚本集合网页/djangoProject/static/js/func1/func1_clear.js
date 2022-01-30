// 清除所有框中的内容
$(function () {
    $("#clear_button").click(function () {
        // 方法1
        // $("#sql").val("");

        // 方法2
        document.getElementById("sql").value = "";
        $("#result1").val("");
        $("#result2").val("");
        document.getElementById("copy_result").innerHTML = "清空成功";
    })
})

// 复制result1的内容
$(function () {
    $("#copy_result1").click(function () {
        $("#result1").select();
        document.execCommand("copy");
        document.getElementById("copy_result").innerHTML = "复制成功";
    })
})

// 复制result2中的内容
$(function () {
    $("#copy_result2").click(function () {
        $("#result2").select();
        document.execCommand("copy");
        document.getElementById("copy_result").innerHTML = "复制成功";
    })
})