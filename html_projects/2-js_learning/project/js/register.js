// 注册页面的逻辑代码
$('form').on('submit', function(e){
    // 1. 阻止默认行为
    e.preventDefault();
    // 2. 采集用户信息
    const data = $('form').serialize()
    console.log(data);
    // 3. 发送请求
    $.post('http://10.193.68.138:8000/manage/register/', data, res=>{
        console.log(res);
        // 4. 判断结果，来决定是否提示错误
        if(res.status === 0) {
            // 提示错误
            $('form>span').css('display', 'block')
            $('form>span').text(res.msg)
            return 
        }
        // 5. 跳转页面；代码执行到这里，表示注册成功了
        window.alert('恭喜注册成功，点击确定跳转到登录页')
        window.location.href = './login.html'
    })
})