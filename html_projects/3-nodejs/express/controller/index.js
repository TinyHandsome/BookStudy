const list = (req, res, next) => {
    // let data = '<ul>'
    // for (let i = 0; i < 100; i++) {
    //     data += `<li>line ${i}</li>`
    // }
    
    // data += '</ul>'
    // res.send(data)

    // let dataObj = {
    //     ret: true,
    //     data: []
    // }
    // for(var i = 0; i<100; i++) {
    //     dataObj.data.push('line' + i)
    // }
    // res.send(dataObj)

    let dataArray = []
    for (let i = 0; i < 100; i++) {
        dataArray.push('line' + i)
    }
    res.render('list', {
        data: JSON.stringify(dataArray)
    })
}
    
exports.list = list