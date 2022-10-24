const path = require('path');
const mime = require('mime');
const fs = require('fs');


function myReadFile(file) {
    return new Promise((resolve, reject) => {
        fs.readFile(file, (err, data) => {
            if (err) {
                resolve('You visit a folder that index.html not in. / 你访问的文件夹里面没有index.html')
            } else {
                resolve(data)
            }
        })
    })
}

async function readStaticFile(filePathName) {
    let ext = path.parse(filePathName).ext
    // 如果前面的值为none，则取后面的值
    let mimeType = mime.getType(ext) || 'text/html'
    let data

    // 判断文件是否存在
    if (fs.existsSync(filePathName)) {
        if (ext) {
            // await myReadFile(filePathName).then(result => data = result)
            //     .catch((err) => data = err)
            data = await myReadFile(filePathName)
        } else {
            // await myReadFile(path.join(filePathName, '/index.html')).then(result => data = result)
            //     .catch((err) => data = err)
            data = await myReadFile(path.join(filePathName, '/index.html'))
        }
    } else {
        // console.log('file is not found');
        // res.end('file not found')
        data = 'file or folder not found'
    }

    return {
        data,
        mimeType
    }
}

module.exports = readStaticFile