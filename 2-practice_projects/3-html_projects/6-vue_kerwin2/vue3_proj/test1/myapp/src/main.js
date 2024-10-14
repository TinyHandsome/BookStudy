import { createApp } from 'vue'
// import './style.css'
import App from './24-pinia/App.vue'
import router from './24-pinia/router'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// 1. 引入需要的组件
import {Button} from 'vant'
// 2. 引入组件样式
import 'vant/lib/index.css'

// 导入配置文件
import "./24-pinia/util/config"

const pinia = createPinia()
var app = createApp(App)

// 注册路由
app.use(router)
app.use(pinia)
app.use(Button)
app.use(ElementPlus)
app.mount('#app')
