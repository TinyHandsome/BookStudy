const http = require('http')

const server = http.createServer((request, response) => {
    console.log(request);
})

server.listen(8080, () => {
    console.log('localhost:8080');
})