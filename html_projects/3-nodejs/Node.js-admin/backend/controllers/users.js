const usersModel = require('../models/users');
const { hash } = require('../utils/tools');

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
    const { username, _password } = req.body
    let result = await usersModel.findUser(username)

    if (result) {
        let { password } = result
    } else {
        res.render('success', {
            data: JSON.stringify({
                message: '用户名错误'
            })
        })
    }

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

exports.signup = signup
exports.signin = signin
exports.list = list
exports.remove = remove
