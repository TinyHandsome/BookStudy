const path = require('path');
const express = require('express');
const app = express()

const bodyParser = require('body-parser');

const router = require('./router/index');

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

// 静态资源
app.use(express.static('./public'))

// view engine setup
app.engine('art', require('express-art-template'))
app.set('view', {
    debug: process.env.NODE_ENV !== 'production'
})
app.set('view', path.join(__dirname, 'views'))
app.set('view engine', 'art')

app.use('/', router)

app.listen(8088, () => {
    console.log('localhost:8088');
})