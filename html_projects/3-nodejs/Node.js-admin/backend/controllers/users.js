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

// 用户列表
const list = async (req, res) => {
    res.set('content-type', 'application/json;charset=utf-8')

    const listResult = await usersModel.findList()
    res.render('success', {
        data: JSON.stringify(listResult)
    })
}

exports.signup = signup
exports.list = list