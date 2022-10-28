const express = require('express');
const app = express()

const bodyParser = require('body-parser');

const router = require('./router/index');

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

// 静态资源
app.use(express.static('./public'))

app.use('/', router)

app.listen(8088, () => {
    console.log('localhost:8088');
})