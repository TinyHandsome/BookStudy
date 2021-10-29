$(function (){
    $(".order").click(function (){
        var $order = $(this);
        var order_id = $order.attr("orderid");

        window.open('/axf/orderdetail/?orderid=' + order_id, target="_self");
    })
})