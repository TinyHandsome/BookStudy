// 修改密码的逻辑
// 1. 验证登录
const jwt_token = window.localStorage.getItem('jwt_token')

if (!jwt_token) {
    window.location.href = './login.html'
} else {
    getInfo()
}

// 2. 获取用户信息
function getInfo() {
    // 直接发送请求，请求个人信息
    $.ajax({
        url: 'http://10.193.68.138:8000/manage/getcurrentuserinfo/',
        method: 'GET',
        headers: {
            authorization: jwt_token
        },
        success(res) {
            if (res.status !== 1) {
                window.location.href = './login.html'
            }
        },
        error(res) {
            alert('获取失败，请检查服务器')
        }
    })
}

// 3. 表单提交发送请求，修改密码
$('form').on('submit', function (e) {
    // 3.1 阻止默认行为
    e.preventDefault();

    // 3.2 采集用户信息
    const data = $('form').serialize()

    // 3.3 发送请求
    $.ajax({
        url: 'http://10.193.68.138:8000/manage/updatepassword/',
        method: 'POST',
        data: data,
        headers: { authorization: jwt_token },
        success(res) {
            var temp = $('form>span');
            if (res.status !== 1) {
                temp.text(res.msg);
                temp.css('display', 'block');
                return
            } else {
                temp.css('display', 'none');
            }

            // 3.5 提示用户修改密码成功
            window.alert('修改密码成功，点击确定跳转回登录页')
            window.location.href = './login.html'
        }
    })
})