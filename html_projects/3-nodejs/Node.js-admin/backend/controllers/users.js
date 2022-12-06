const usersModel = require('../models/users');
const { hash, compare, sign, verify } = require('../utils/tools');
// const randomstring = require('randomstring');

// 注册用户
const signup = async (req, res, next) => {
    // res.send('hello')
    const { username, password } = req.body

    //  密码加密
    const bcryptPassword = await hash(password)

    // 判断用户是否存在
    let findResult = await usersModel.findUser(username)
    // console.log(findResult);

    res.set('content-type', 'application/json;charset=utf-8')

    if (findResult) {
        res.render('fail', {
            data: JSON.stringify({
                message: '用户名存在'
            })
        })
    } else {
        // 用户不存在就注册一个该用户
        let result = await usersModel.signup({
            username,
            password: bcryptPassword
        })

        res.render('success', {
            data: JSON.stringify({
                message: '注册成功'
            })
        })
    }
}

// 用户登录
const signin = async (req, res, next) => {
    const { username, password } = req.body
    let result = await usersModel.findUser(username)

    // 验证用户是否是合法用户
    if (result) {
        let { password: hash } = result
        let compareResult = await compare(password, hash)
        if (compareResult) {
            // const sessionId = randomstring.generate()
            // res.set('Set-Cookie', `sessionId=${sessionId}; Path=/; HttpOnly`)

            // req.session.username = username
            // console.log(req.session);

            const token = sign(username)
            res.set('X-Access-Token', token)

            res.render('success', {
                data: JSON.stringify({
                    username
                })
            })

        } else {
            // 密码错误
            res.render('fail', {
                data: JSON.stringify({
                    message: '用户名或密码错误'
                })
            })
        }
    } else {
        // 用户名错误
        res.render('fail', {
            data: JSON.stringify({
                message: '用户名或密码错误'
            })
        })
    }
}

// 用户登出
const signout = async (req, res, next) => {
    req.session = null
    res.render('success', {
        data: JSON.stringify({
            message: '成功退出登录'
        })
    })
}

// 用户列表
const list = async (req, res, next) => {
    res.set('content-type', 'application/json;charset=utf-8')

    const listResult = await usersModel.findList()
    res.render('success', {
        data: JSON.stringify(listResult)
    })
}

// 删除用户
const remove = async (req, res, next) => {
    const { id } = req.body
    let result = await usersModel.remove(id)
    // console.log(result);
    if (result) {
        res.render('success', {
            data: JSON.stringify({
                message: '用户删除成功'
            })
        })
    } else {
        res.render('fail', {
            data: JSON.stringify({
                message: '用户删除失败'
            })
        })
    }
}

// 验证用户登录状态
const isAuth = async (req, res, next) => {
    let token = req.get('X-Access-Token')
    try {
        let result = verify(token)
        // console.log(result);
        res.render('success', {
            data: JSON.stringify({
                username: result.username
            })
        })

    } catch (e) {
        res.render('fail', {
            data: JSON.stringify({
                message: '请登录'
            })
        })
    }

    // if (req.session.username) {
    //     res.render('success', {
    //         data: JSON.stringify({
    //             username: req.session.username
    //         })
    //     })
    // } else {
    //     res.render('fail', {
    //         data: JSON.stringify({
    //             message: '请登录'
    //         })
    //     })
    // }
}

exports.signup = signup
exports.signin = signin
exports.list = list
exports.remove = remove
exports.signout = signout
exports.isAuth = isAuth