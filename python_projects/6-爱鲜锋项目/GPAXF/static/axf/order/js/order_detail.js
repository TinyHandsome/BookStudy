$(function (){
    $('#alipay').click(function (){
        console.log("支付");
        var orderid = $(this).attr("orderid");
        $.getJSON("/axf/payed/", {"orderid": orderid}, function (data){
            console.log(data);
            if (data['status'] === 200){
                window.open('/axf/mine/', target="_self");
            }
        })
    })
})