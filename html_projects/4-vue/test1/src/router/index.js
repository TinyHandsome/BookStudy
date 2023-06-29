import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Films from '@/views/Films.vue'
import Cinemas from '@/views/Cinemas.vue'
import Center from '@/views/Center.vue'

// 注册两个全局组件 router-view router-link
Vue.use(VueRouter)

// 配置表
const routes = [
  {
    path: '/films',
    component: Films
  },
  {
    path: '/cinemas',
    component: Cinemas
  },
  {
    path: '/center',
    component: Center
  },

  // 重定向
  {
    path: '*',
    redirect: '/films'
  }
]

// const routes = [
//   {
//     path: '/',
//     name: 'home',
//     component: HomeView
//   },
//   {
//     path: '/about',
//     name: 'about',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
//   }
// ]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
