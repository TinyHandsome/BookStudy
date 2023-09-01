const crypto = require('crypto');
const password = 'abc123'

const hash = crypto.createHash('sha1').update(password, 'utf-8').digest('hex')

console.log(hash);