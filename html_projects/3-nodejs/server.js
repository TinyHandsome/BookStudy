const http = require('http')
const querystring = require('querystring')
const https = require('https');

const server = http.createServer((request, response) => {
    // console.log(response);

    // const url = request.url
    // console.log(url);

    https.get('https://www.xiaomiyoupin.com/mtop/mf/cat/list', (result) => {
        let data = ''
        result.on('data', (chunk) => {
            data += chunk
        })
        result.on('end', () => {
            response.writeHead(200, {
                // 'content-type': 'text/html'
                'content-type': 'application/json;charset=utf-8'
            })
            // response.write('<div>hello</div>')
            // response.write('{"x": 1}')
            // response.end('{"x": 1}')
            // console.log(data);
            // response.write(`{"url": "${url}"}`)
            response.write(JSON.stringify(querystring.parse(data)))
            response.end()
        })
    })
})

server.listen(8080, () => {
    console.log('localhost:8080');
})