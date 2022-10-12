const http = require('http')

const server = http.createServer((request, response) => {
    // console.log(response);
    request.on('data', (chunk) => {
        data += chunk
    })

    const url = request.url
    // console.log(url);

    response.writeHead(404, {
        // 'content-type': 'text/html'
        'content-type': 'application/json;charset=utf-8'
    })
    // response.write('<div>hello</div>')
    // response.write('{"x": 1}')
    // response.end('{"x": 1}')
    
    
    response.write(`{"url": "${url}"}`)
    response.end()
})

server.listen(8080, () => {
    console.log('localhost:8080');
})