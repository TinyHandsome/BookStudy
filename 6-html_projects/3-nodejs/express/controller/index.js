var template = require('art-template');
var path = require('path');
var fs = require('fs');
var jwt = require('jsonwebtoken');

const listModel = require('../model/list');

const list = (req, res, next) => {
    // let data = '<ul>'
    // for (let i = 0; i < 100; i++) {
    //     data += `<li>line ${i}</li>`
    // }
    
    // data += '</ul>'
    // res.send(data)

    // let dataObj = {
    //     ret: true,
    //     data: []
    // }
    // for(var i = 0; i<100; i++) {
    //     dataObj.data.push('line' + i)
    // }
    // res.send(dataObj)

    // let dataArray = []
    // for (let i = 0; i < 1000; i++) {
    //     dataArray.push('line' + i)
    // }

    // res.set('content-type', 'application/json;charset=utf-8')
    // res.header('Content-Type', 'application/json;charset=utf-8')

    // res.render('list', {
    //     data: JSON.stringify(dataArray)
    // })

    // res.render('list-html', {
    //     data: dataArray
    // })

    var html = template(path.join(__dirname, '../view/list-html.art'), {
        data: listModel.dataArray
    })
    fs.writeFileSync(path.join(__dirname, '../public/list.html'), html)
    // console.log(html);
    res.send(html)
}

const token = (req, res, next) => {
    // res.send('ok')

    // 对称加密
    const token = jwt.sign({username: 'admin'}, 'hahaha')
    // res.send(token)
    const result = jwt.verify(token, 'hahaha')
    // res.send(result)

    // 非对称加密
    const privateKey = fs.readFileSync(path.join(__dirname, '../keys/rsa_private_key.pem'))
    const tk = jwt.sign({username: 'admin'}, privateKey, {algorithm: 'RS256'})
    const publicKey = fs.readFileSync(path.join(__dirname, '../keys/rsa_public_key.pem'))
    const result2 = jwt.verify(tk, publicKey)
    res.send(result2)

}
    
exports.list = list
exports.token = token