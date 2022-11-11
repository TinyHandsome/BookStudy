import indexTpl from '../views/index.art'
import signinTpl from '../views/signin.art'
import usersTpl from '../views/users.art'

const htmlIndex = indexTpl({})
const htmlSignin = signinTpl({})

const _handleSubmit = (router) => {
    return (e) => {
        e.preventDefault();
        router.go('/index')
    }
}

const _signup = () => {
    const $btnClose = $('#users-close')

    // 提交表单
    const data = $('#users-form').serialize()
    $.ajax({
        url: '/api/users/signup',
        type: 'post',
        data: data,
        success(res) {
            console.log(res);
        }
    })

    $btnClose.click()
}

const signin = (router) => {
    return (req, res, next) => {
        res.render(htmlSignin)

        $('#signin').on('submit', _handleSubmit(router))
    }
}

const signup = () => {}

const index = (router) => {
    return (req, res, next) => {
        res.render(htmlIndex)

        // 让页面撑满整个屏幕
        $(window, '.wrapper').resize()

        // 填充用户列表
        $('#content').html(usersTpl())

        // 点击保存，提交表单
        $('#users-save').on('click', _signup)
    }
}

export {
    signin,
    signup,
    index
}