const express = require('express');

const app = express()

app.use('/api', (req, res) => {
    res.send('world')
})

app.use('/', (req, res) => {
    console.log(0);
    res.send('hello')
}, )

app.listen(8080, () => {
    console.log('asdasd');
})