const http = require('http')
const https = require('https')
const cheerio = require('cheerio')

function filterData(data) {
    const $ = cheerio.load(data)
    // console.log(data);

    $('.section-item-box p').each((index, el) => {
        console.log(index);
        console.log($(el).text());
    })
}

const server = http.createServer((req, res) => {
    let data = ''
    https.get('https:www.meizu.com', (result) => {
        result.on('data', (chunk) => {
            data += chunk
        })
        result.on('end', () => {
            filterData(data)
        })
    })
})

server.listen(8080, () => {
    console.log('localhost:8080');
})