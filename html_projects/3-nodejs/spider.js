const http = require('http')
const https = require('https')

const server = http.createServer((req, res) => {
    let data = ''
    https.get('https:www.meizu.com', (result) => {
        result.on('data', (chunk) => {
            console.log(chunk.toString());
        })
        result.on('end', () => {

        })
    })
})

server.listen(8080, () => {
    console.log('localhost:8080');
})