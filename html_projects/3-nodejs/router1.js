const fs = require('fs');
const mime = require('mime')
// require('http').createServer((req, res) => {
//     // res.end('ok')
//     const urlString = req.url
//     switch (urlString) {
//         case '/':
//             res.end('hello')
//             break;
//         case '/home':
//             fs.readFile('./home.html', (err, content) => {
//                 res.end(content)
//             })
//             break;
//         case '/home.js':
//             fs.readFile('./home.js', (err, content) => {
//                 res.end(content)
//             })
//             break
//         case '/pics/a.png':
//             fs.readFile('./pics/a.png', (err, content) => {
//                 res.end(content)
//             })
//             break
//         default:
//             res.end('page 404')
//     }
// })

require('http').createServer((req, res) => {
    const urlString = req.url
    const type = mime.getType(urlString.split('.')[1])
    res.writeHead(200, {
        'content-type': type
    })

    const file = fs.readFileSync(`./${urlString}`)
    res.end(file)
})
    .listen(8088, () => {
        console.log('localhost: 8088');
    })