const fs = require('fs')
const fsPromises = require('fs').promises

// fs.mkdir('logs', (err) => {
//     if(err) throw err
//     console.log('文件夹创建成功');
// })

// fs.rename('./logs', './new_log', () => {
//     console.log('文件夹名字修改成功');
// })

// fs.rmdir('./new_log', ()=>{
//     console.log('删除成功');
// })

// fs.readdir('./logs', (err, result) => {
//     console.log(result);
// })

// fs.writeFile('./logs/log1.log', 'hello \n world', (err) => {
//     console.log('done');
// })

// fs.appendFile('./logs/log1.log', '!!!', (err) => {
//     console.log('done');
// })

// fs.unlink('./logs/log1.log', (err) => {
//     console.log('done');
// })

// fs.readFile('./logs/log1.log', 'utf-8', (err, result) => {
//     console.log(result.toString());
// })

// ;(async()=>{
//     let result = await fsPromises.readFile('./logs/log1.log')
//     console.log(result.toString());
// })()

// for(var i=0; i < 10; i++) {
//     fs.writeFile(`./logs/log-${i}.log`, `log-${i}`, (err) => {
//         console.log('done');
//     })
// }


// fs.readdir('./', (err, content) => {
//     console.log(content);
//     content.forEach((value, index) => {
//         fs.stat(`./${value}`, (err, stats) => {
//             console.log(stats);
//             console.log(stats.isDirectory())
//         });
//     })
// })

// 递归获取文件目录下所有文档的内容
// function readDir(dir) {
//     fs.readdir(dir, (err, content) => {
//         content.forEach((value, index) => {
//             let joinDir = `${dir}/${value}`
//             fs.stat(joinDir, (err, stats) => {
//                 if (stats.isDirectory()) {
//                     readDir(joinDir)
//                 } else {
//                     fs.readFile(joinDir, 'utf-8', (err, content) => {
//                         console.log(content);
//                     })
//                 }
//             })
//         })
//     })
// }

// readDir('./')


fs.watch('./logs/log-0.log', (err) => {
    console.log('file has changed');
})
