const bcrpt = require('bcrypt');

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