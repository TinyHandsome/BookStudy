const http = require('http');
const path = require('path');
const readStaticFile = require('./fileStatic');

http.createServer(async (req, res) => {
    // 这里url就是访问的url，例子中为index.html，如果不是该路径，其他的也有容错处理
    let urlString = req.url
    let filePathName = path.join(__dirname, './public', urlString)
    console.log(filePathName);

    let { data, mimeType } = await readStaticFile(filePathName)

    res.writeHead(200, {
        'content-type': `${mimeType}; charset=utf-8`
    })
    res.write(data)
    res.end()
}).listen(8888, () => {
    console.log('visit success');
})