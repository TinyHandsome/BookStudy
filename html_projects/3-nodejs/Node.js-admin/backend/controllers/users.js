// 注册用户
const signup = (req, res, next) => {
    // res.send('hello')
    const {username, password} = req.body
    res.render('success', {
        data: JSON.stringify({
            username,
            password
        })
    })
}

exports.signup = signup