const path = require('path');
const multer = require('multer');
const mime = require('mime');
const fs = require('fs');

// const upload = multer({
//     dest: path.join(__dirname, '../public/uploads')
// })
// let fn = ''

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, path.join(__dirname, '../public/uploads'))
    },
    filename: function (req, file, cb) {
        let ext = mime.getExtension(file.mimetype)
        let fn = file.fieldname + '-' + Date.now() + '.' + ext
        cb(null, fn)
    }
})

const limits = {
    fileSize: 200000,
    files: 1
}

function fileFilter(req, file, cb) {
    // 这个函数应该调用 cb ，用boolean值来指示是否应该接收该文件
    const acceptType = [
        'image/png',
        'image/jpg',
        'image/jpeg',
        'image/gif'
    ]
    if (!acceptType.includes(file.mimetype)) {
        // 如果有问题，你可以总是这样发送一个错误
        cb(new Error('文件类型必须是.png | .jpg | .gif'))
    } else {
        // 接收文件
        cb(null, true)
    }
}

const upload = multer({
    storage,
    limits,
    fileFilter
}).single('companyLogo')

const uploadMiddleware = (req, res, next) => {
    multer()
    upload(req, res, function (err) {
        if (err instanceof multer.MulterError) {
            // 发生错误
            res.render('fail', {
                data: JSON.stringify({
                    message: '文件超出200k'
                })
            })
        } else if (err) {
            // 发生错误
            res.render('fail', {
                data: JSON.stringify({
                    message: err.message
                })
            })
        } else {
            // 一切都好
            const { companyLogo_old } = req.body
            if (req.file && companyLogo_old) {
                try {
                    fs.unlinkSync(path.join(__dirname, `../public/uploads/${companyLogo_old}`))
                    req.companyLogo = req.file.filename
                } catch (err) {
                    console.log(err);
                }
            } else if (!req.file && companyLogo_old){
                req.companyLogo = companyLogo_old
            } else {
                req.companyLogo = req.file.filename
            }

            next()
        }
    })
}

module.exports = uploadMiddleware 