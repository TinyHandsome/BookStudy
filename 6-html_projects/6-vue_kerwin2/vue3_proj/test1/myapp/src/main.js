import { createApp } from 'vue'
// import './style.css'
import App from './22-router/App.vue'
import router from './22-router/router'

var app = createApp(App)

// 注册路由
app.use(router)
app.mount('#app')
