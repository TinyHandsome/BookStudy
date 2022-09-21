// 登录页面的逻辑代码

$('form').on('submit', function(e){
    // 1. 阻止默认事件
    e.preventDefault();
    // 2. 采集用户信息
    const data = $('form').serialize()
    // 3. 发送请求
    $.post('http://10.193.68.138:8000/manage/login/', data, res => {
        // 4. 判断登录失败
        if (res.status === 0) {
            // 提示错误
            $('form>span').css('display', 'block')
            $('form>span').text(res.msg)
            return
        }
        // // 5. 登录成功
        // // 直接跳转到首页
        // window.location.href = './index.html'
        
        // 5.1 把登录过的“凭证”存储起来，为了其他页面使用
        window.localStorage.setItem('token', res.token)
        // 5.2 把用户的id信息也存储起来
        // window.localStorage.setItem('id', res.user.id)

        // 这里，可以直接把user_id和first_name传过来（我的备注）
        window.localStorage.setItem('user_id', res.user_id)
        let user_name = res.user_name

        if (!user_name){
            user_name = res.username
        }
        window.localStorage.setItem('user_name', user_name)

        // 5.3 跳转页面
        window.location.href = './index.html'
    })
})