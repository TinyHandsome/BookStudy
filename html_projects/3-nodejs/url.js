var log4js = require('log4js')
// logger.lever = 'debug'
log4js.configure({
    appenders: {
        cheese: {
            type: 'file',
            filename: 'cheee.log'
        }
    },
    categories: {
        default: {
            appenders: ['cheese'],
            level: "debug"
        }
    }
})
var logger = log4js.getLogger('cheese')


const url = require('url')
const urlString = 'https://www.baidu.com:443/path/index.html?id=2#tag=3'

logger.debug(url.parse(urlString));
logger.debug(url.format(
    {
        protocol: 'https:',
        slashes: true,
        auth: null,
        host: 'www.baidu.com:443',
        port: '443',
        hostname: 'www.baidu.com',
        hash: '#tag=3',
        search: '?id=2',
        query: 'id=2',
        pathname: '/path/index.html',
        path: '/path/index.html?id=2',
        href: 'https://www.baidu.com:443/path/index.html?id=2#tag=3'

    }
))

logger.debug(url.resolve('http://www.abc.com/a', '../'))
logger.debug(url.resolve('http://www.abc.com/a', '/b'))


const urlParams = new URLSearchParams(url.parse(urlString).search)
logger.debug(urlParams);

const querystring = require('querystring')
const query = 'id=2&name=tongyi&from=北京'
const query2 = 'id:2/name:tongyi/from:北京'
const queryEscape = 'id%3D2%26name%3Dtongyi%26from%3D%E5%8C%97%E4%BA%AC'
const queryObj = {
    id: 2,
    name: 'tongyi',
    from: '北京'
}

console.log(querystring.parse(query));
console.log(querystring.escape(query));
console.log(querystring.unescape(queryEscape));
console.log(querystring.stringify(queryObj, ':', '/'));
console.log(querystring.parse(query2, '/', ':'));
const newQuery = querystring.stringify(queryObj, null, null, {
    encodeURIComponent(string){
        return querystring.unescape(string)
    }
})
console.log(newQuery);

var qs = 'x=3&y=4'
var parsed = querystring.parse(qs)
console.log(parsed)