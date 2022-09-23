// 个人中心的逻辑代码
// 1. 验证登录，如果没有登陆过，那么不会展示该页面
const jwt_token = window.localStorage.getItem('jwt_token')


// 2. 判断token和id是否存在
if (!jwt_token) {
    window.location.href = './login.html'
} else {
    // 才是登录过的状态
    getInfo()
}


// 3. 获取用户信息
function getInfo() {
    // 3.1 发送请求请求用户信息
    $.ajax({
        url: 'http://10.193.68.138:8000/manage/getcurrentuserinfo/',
        method: 'GET',
        headers: {
            authorization: jwt_token
        },
        success(res) {
            // 3.2 判断是否注销过一次登录
            if (res.status !== 1){
                window.location.href = './login.html'
                return
            }else{
                // 可以进行后续操作了
                console.log(res)
                // 把用户信息进行展示
                $('form .username').val(res.data.user_code)
                $('form [name=user_name]').val(res.data.user_name)
                $('form [name=user_type]').val(res.data.user_type)
                $('form [name=user_age]').val(res.data.user_age)
                $('form [name=user_gender]').val(res.data.user_gender)
            }
        }
    })
}

// 4. 修改个人信息
$('form').on('submit', function(e){
    // 4.1 阻止默认行为
    e.preventDefault()
    // 4.2 采集用户信息
    const data = $('form').serialize()
    // 4.3 发送请求
    $.ajax({
        url: 'http://10.193.68.138:8000/manage/updateuser/',
        method: 'POST',
        data: data,
        headers: { authorization: jwt_token },
        success(res){
            // console.log(res);
            window.alert('修改用户信息成功')
        }
    })
})