import signinTpl from '../views/signin.art'
const htmlSignin = signinTpl({})
import { signin as signinModel } from '../models/signin'

const _handleSubmit = (router) => {
    return async (e) => {
        e.preventDefault();

        // 提交表单
        const data = $('#signin').serialize()
        let result = await signinModel(data)
        const token = result.jqXHR.getResponseHeader('X-Access-Token')
        localStorage.setItem('lg-token', token)
        if (result.res.ret) {
            router.go('/index')
        }
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