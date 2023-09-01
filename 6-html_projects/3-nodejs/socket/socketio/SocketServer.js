var express = require('express')
var app = express();
var http = require('http').createServer(app);
var io = require('socket.io')(http);


app.use(express.static('./public'))

app.get('/', (req, res) => {
    // res.sendFile(__dirname + '/index.html')
    res.send('hello')
})

io.on('connection', (socket) => {
    console.log('a user connected');

    socket.on('receive', (data) => {
        // console.log(data);
        socket.broadcast.emit('message', data)
    })
})

http.listen(3000, '10.193.68.138', () => {
    console.log('listening onn *:3000');
})