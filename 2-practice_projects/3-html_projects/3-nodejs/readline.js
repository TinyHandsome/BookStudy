const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.question('你如何看到你爹', (answer) => {
    // 记录
    console.log(`thx for your answer: ${answer}`);
    rl.close()
})