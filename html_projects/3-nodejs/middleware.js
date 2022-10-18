const http = require('http')
const url = require('url')
const { createProxyMiddleware } = require('http-proxy-middleware')

const server = http.createServer((req, res) => {
    let urlStr = req.url
    if (/\/api/.test(urlStr)) {
        // console.log(urlStr);
        const proxy = createProxyMiddleware('/api', {
            target: 'https://silkroad.csdn.net/',
            changeOrigin: true
        })

        proxy(req, res)
    } else if (/\/aaa/.test(urlStr)) {
        const proxy2 = createProxyMiddleware('/aaa', {
            target: 'https://blog.csdn.net/',
            changeOrigin: true,
            pathRewrite: {
                '^/aaa': ''
            }
        })

        proxy2(req, res)

    } 
    else {
        console.log('error');
    }
})

server.listen(8070, () => {
    console.log('localhost:8070');
})