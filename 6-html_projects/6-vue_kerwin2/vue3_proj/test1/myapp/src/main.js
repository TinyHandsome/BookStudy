import { createApp } from 'vue'
// import './style.css'
import App from './23-vuex/App.vue'
import router from './23-vuex/router'
import store from './23-vuex/store'

var app = createApp(App)

// 注册路由
app.use(router)
app.use(store)
app.mount('#app')
