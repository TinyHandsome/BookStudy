$(function () {
    $("#all_types").click(function () {
        console.log("全部类型");

        var $all_types_container = $("#all_types_container");
        $all_types_container.show();
    })

    $("#sort_rule").click(function () {
        console.log("排序规则");
        var $sort_rule_container = $("#sort_rule_container");
        $sort_rule_container.slideDown(10000);
    })
})