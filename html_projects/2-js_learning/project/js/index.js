/*

// 首页的逻辑代码
// 问题：如何在首页知道我登录成功了？
// 通过登录成功以后存储的凭证来证明
// 1. 拿到localStorage内的凭证
const token = window.localStorage.getItem('token')
const id = window.localStorage.getItem('id')

// 2. 判断token和id是否存在
if (!token || !id) {
    // 表示你还没有登录过
    // 不需要展示登录后的内容
    $('.off').addClass('active')
    $('.on').removeClass('active')
} else {
    // 表示登录过
    // 我们应该请求用户信息，把用户昵称展示出来
    getInfo()
}

// 3. 请求用户信息
function getInfo() {
    // 3.1 发送请求请求用户信息
    $.ajax({
        url: 'http://10.193.68.138:8000/manage/getcurrentuserinfo/',
        method: 'GET',
        data: { id: id },
        headers: {
            authorization: token
        },
        success(res) {
            // 3.2 判断是否登录
            if (res.status !== 1) {
                $('.off').addClass('active')
                $('on').removeClass('active')
                return
            } else {
                $('.on').addClass('active').find('span').text(res.info.nickname)
                $('.off').removeClass('active')
            }
        }
    })
}
*/

// 下面为华子平台登录逻辑处理
const jwt_token = window.localStorage.getItem('jwt_token')

$.ajax({
    url: 'http://10.193.68.138:8000/manage/getcurrentuserinfo/',
    method: 'GET',
    headers: {
        authorization: jwt_token
    },
    success(res) {
        if (res.status !== 1) {
            $('.off').addClass('active')
            $('on').removeClass('active')
            return
        } else {
            let user_name = res.data.user_name
            $('.off').removeClass('active')
            $('.on').addClass('active').find('span').text(user_name)
        }
    },
    error(res) {
        alert('获取失败，请检查服务器')
    }
})

$('button.self').on('click', function(){
    window.location.href = './self.html'
})

// 退出登录
$('button.logout').on('click', function () { 
    // 删掉window.localStorage的信息
    window.localStorage.clear()
    // 直接发送请求，请求退出
    $.get('http://10.193.68.138:8000/manage/logout/', res => {
        // 退出登录以后，直接刷新页面
        window.location.reload()
    })
 })