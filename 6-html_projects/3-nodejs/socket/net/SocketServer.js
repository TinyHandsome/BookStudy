const net = require('net');

let clients = {}
let clientName = 0

const server = new net.createServer()

// const server = net.createServer((client) => {
server.on('connection', (client) => {
    // socket.end('goodby\n')

    client.name = ++clientName
    clients[client.name] = client

    // client.write('hello')
    client.on('data', (chunk) => {
        // console.log(chunk.toString());
        // console.log(11111, chunk.toString());
        broadcast(client, chunk.toString())
    })

    client.on('error', (e) => {
        console.log('client error' + e);
        client.end()
    })

    client.on('close', () => {
        delete clients[client.name]
        console.log(client.name + ' 下线了');
    })
})

// server.on('error', (err) => {
//     throw err
// })

// server.listen('9527', () => {
//     console.log('opened server on', server.address());
// })

function broadcast(client, msg) {
    for (var key in clients) {
        clients[key].write(client.name + ' 说: ' + msg)
    }
}

server.listen(9527, 'localhost')