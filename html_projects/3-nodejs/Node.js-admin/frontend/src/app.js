import indexTpl from './views/index.art'
import signinTpl from './views/signin.art'

console.log(indexTpl);
// const html = indexTpl({})
const html = signinTpl({})

$('#root').html(html)