import { createApp } from 'vue'
// import ElementUI from 'element-plus'
import App from './App.vue'
// import App from './App.vue'
import router from './router'
import store from './store'
// import "element-plus/theme-chalk/index.css"

import Vant from 'vant'
import 'vant/lib/index.css'

createApp(App)
    .use(Vant)
    .use(store)
    .use(router)
    .mount('#app')
