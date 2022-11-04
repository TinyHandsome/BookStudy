const net = require('net');

const server = net.createServer((socket) => {
    // socket.end('goodby\n')
    socket.write('hello')

})

server.on('error', (err) => {
    throw err
})

server.listen('9527', () => {
    console.log('opened server on', server.address());
})