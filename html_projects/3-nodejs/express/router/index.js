const express = require('express');
const { list } = require('../controller/index');
// 路由中间件
const router = express.Router()

router.get('/', list)

// router.get('/index', (req, res, next) => {
//     const query = req.query
//     console.log(query);
//     // res.send(query)
//     res.json(query)
// })

// router.post('/index', (req, res, next) => {
//     const data = req.body
//     console.log(data);
//     res.send(data)
// })

// router.put('/index', (req, res, next) => {
//     res.send('put data')
// })

// router.all('/index', (req, res, next) => {
//     res.send('hello')
// })

module.exports = router