import { createApp } from 'vue'
// import './style.css'
import App from './19-vca/App.vue'

var app = createApp(App)
app.directive('kerwin', {
    // 指令的钩子
    mounted(el) {
        console.log("当前节点插入到父节点的时候调用", el);
        el.style.background = "yellow"
    }
})
app.mount('#app')
