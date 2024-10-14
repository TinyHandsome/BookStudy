const bcrpt = require('bcrypt');
const fs = require('fs');
const path = require('path');
const jwt = require('jsonwebtoken');

exports.hash = (myPlaintextPassword) => {
    return new Promise((resolve, reject) => {
        bcrpt.genSalt(10, function (err, salt) {
            bcrpt.hash(myPlaintextPassword, salt, function (err, hash) {
                if (err) {
                    reject(err)
                }
                resolve(hash)
            })
        })
    })
}

exports.compare = (myPlaintextPassword, hash) => {
    return new Promise((resolve, reject) => {
        bcrpt.compare(myPlaintextPassword, hash, function (err, result) {
            resolve(result)
        })
    })
}

exports.sign = (username) => {
    const privateKey = fs.readFileSync(path.join(__dirname, '../keys/rsa_private_key.pem'))   
    const token = jwt.sign({username}, privateKey, {algorithm: 'RS256'})
    return token
}

exports.verify = (token) => {
    const publicKey = fs.readFileSync(path.join(__dirname, '../keys/rsa_public_key.pem'))   
    const result = jwt.verify(token, publicKey)
    return result
}