import signinTpl from '../views/signin.art'
const htmlSignin = signinTpl({})

const _handleSubmit = (router) => {
    return (e) => {
        e.preventDefault();

        // 提交表单
        const data = $('#signin').serialize()
        $.ajax({
            url: '/api/users/signin',
            type: 'post',
            dataType: 'json',
            data: data,
            success: (res) => {
                if (res.ret) {
                    router.go('/index')
                }
            },
            error: (res) => {
                console.log(res);
            }
        })
    }
}


// 登录模块
const signin = (router) => {
    return (req, res, next) => {
        res.render(htmlSignin)
        $('#signin').on('submit', _handleSubmit(router))
    }
}

export default signin