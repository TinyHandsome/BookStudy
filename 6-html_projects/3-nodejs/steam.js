const fs = require('fs')
const zlib = require('zlib');

const gzip = zlib.createGzip()

const readStream = fs.createReadStream('./logs/log1.log')
const writeStream = fs.createWriteStream('./logs/logs.gzip')

readStream
.pipe(gzip)
.pipe(writeStream)
