import Vue from 'vue'
// import App from './PCApp.vue'
import App from './App.vue'
import router from './router'
import store from './store'



Vue.config.productionTip = false

new Vue({
    router,
    store,
    // vue支持的新写法
    render: (h) => h(App)
}).$mount('#app')

const obj = {
    name: 'kerwin',
    age: 100
}

console.log(obj)
