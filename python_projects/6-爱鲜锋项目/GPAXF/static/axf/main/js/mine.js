$(function (){
    $("#not_login").click(function (){
        window.open('/axf/login/', target="_self");
    })

    $("#regis").click(function(){
        window.open('/axf/register/', target="_self");
    })

    $("#not_pay").click(function (){
        window.open('/axf/orderlistnotpay/', target="_self");
    })
})