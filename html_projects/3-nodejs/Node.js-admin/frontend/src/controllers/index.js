import indexTpl from '../views/index.art'
import signinTpl from '../views/signin.art'

const htmlIndex = indexTpl({})
const htmlSignin = signinTpl({})

const _handleSubmit = (router) => {
    return (e) => {
        e.preventDefault();
        router.go('/index')
    }
}

const signin = (router) => {
    return (req, res, next) => {
        res.render(htmlSignin)

        $('#signin').on('submit', _handleSubmit(router))
    }
}

const index = (router) => {
    return (req, res, next) => {
        res.render(htmlIndex)

        // 让页面撑满整个屏幕
        $(window, '.wrapper').resize()
    }
}

export {
    signin,
    index
}