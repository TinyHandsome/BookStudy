const http = require('http')
const url = require('url')

const server = http.createServer((req, res) => {
    let urlstr = req.url

    // true 是为了解析 url中的query为一个字典
    let urlObj = url.parse(urlstr, true)
    switch(urlObj.pathname) {
        case '/api/data':
            res.write(`${urlObj.query.cb}("hello")`)
            break
        default:
            res.write('page not found.')
    }
    res.end()
})

server.listen(8080, ()=>{
    console.log('localhost:8080');
})