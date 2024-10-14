const _ = require('lodash')

function myChunk(arr) {
    let arr2 = _.chunk(arr, 2)
    return arr2
}

// let arr = [4, 5, 6, 7]
// console.log(arr2);

module.exports = myChunk