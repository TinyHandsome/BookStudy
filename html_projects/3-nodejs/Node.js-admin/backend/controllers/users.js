const usersModel = require('../models/users');

// 注册用户
const signup = async (req, res, next) => {
    // res.send('hello')
    const { username, password } = req.body

    // 判断用户是否存在
    let findResult = await usersModel.findUser(username)
    // console.log(findResult);

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
            password
        })

        console.log(result);

        res.render('success', {
            data: JSON.stringify({
                username,
                password
            })
        })
    }
}

exports.signup = signup