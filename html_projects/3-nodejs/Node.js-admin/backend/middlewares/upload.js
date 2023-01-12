const path = require('path');
const multer = require('multer');
const mime = require('mime');

// const upload = multer({
//     dest: path.join(__dirname, '../public/uploads')
// })
let fn = ''

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, path.join(__dirname, '../public/uploads'))
    },
    filename: function (req, file, cb) {
        let ext = mime.getExtension(file.mimetype)
        fn = file.fieldname + '-' + Date.now() + '.' + ext
        cb(null, fn)
    }
})

const limits = {
    fileSize: 200000,
    files: 1
}

const upload = multer({
    storage,
    limits
}).single('companyLogo')

const uploadMiddleware = (req, res, next) => {
    multer()
    upload(req, res, function(err){
        if (err instanceof multer.MulterError) {
            // 发生错误
        } else {
            // 发生错误
        }
        // 一切都好
        next()
    })
}

module.exports = uploadMiddleware 