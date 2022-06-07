// 创建流程
$(function () {
    $("#create_procedule").click(function () {
        var sql = document.getElementById("sql").value;
        var result1 = document.getElementById("result1").value;
        var result2 = document.getElementById("result2").value;
        var schema_table_name = document.getElementById("schema_table_name").value;
        var my_cookie = document.getElementById("my_cookie").value;

        $.ajax({
            url: "/generate_new_hive_schedule/",
            type: "POST",
            data: {
                result1: result1,
                result2: result2,
                schema_table_name: schema_table_name,
                my_cookie: my_cookie
            },
            success: function (res) {
                if (res == -1) {
                    alert_red("运行中出现错误");
                } else {
                    alert_green('创建成功！');
                }
            },
            error: function () {
                alert_red("出现错误");
            }
        });
    })
})

