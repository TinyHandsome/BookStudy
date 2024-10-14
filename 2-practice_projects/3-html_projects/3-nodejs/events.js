const EventEmitter = require('events')

class MyEventEmitter extends EventEmitter { }


const event = new MyEventEmitter()

event.on('play', (value) => {
    console.log(value);
})

event.on('play', (value) => {
    console.log('another' + value);
})


// 触发
event.emit('play', 'movie')
event.emit('play', 'movie')
event.emit('play', 'movie')