import Vue from 'vue'
import VueRouter from 'vue-router'
import Films from '@/views/Films.vue'
import Cinemas from '@/views/Cinemas.vue'
import NowPlaying from '@/views/films/NowPlaying'
import ComingSoon from '@/views/films/ComingSoon'
import Search from '@/views/Search'
import Detail from '@/views/Detail'
import Login from '@/views/Login'

// 注册两个全局组件 router-view router-link
Vue.use(VueRouter)

const Center = () => import("@/views/Center")

// 配置表
const routes = [
  {
    path: '/films',
    component: Films,
    children: [
      {
        path: '/films/nowplaying',
        component: NowPlaying
      },
      {
        path: '/films/comingsoon',
        component: ComingSoon
      },
      {
        path: '/films',
        redirect: '/films/nowplaying'
      }
    ]
  },
  {
    // 动态路由
    name: "detail",  // 命名路由
    path: '/detail/:myid',
    component: Detail
  },
  {
    path: '/cinemas',
    component: Cinemas
  },
  {
    path: '/cinemas/search',
    component: Search
  },
  {
    path: '/center',
    component: Center,
    meta: {
      isRequired: true,
    },
    beforeEach: (to, from, next) => {
      next()
    }
  },
  {
    path: '/order',
    component: () => import("@/views/Order"),
    meta: {
      isRequired: true,
    }
  },
  {
    path: '/login',
    component: Login
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
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 全局拦截
router.beforeEach((to, from, next) => {
  console.log(to.fullPath);
  if (to.meta.isRequired) {
    // 判断 本地存储中 是否有 token 字段
    if (localStorage.getItem('token')) {
      next()
    } else {
      // next("/login")
      next({
        path: "/login",
        query: {
          redirect: to.fullPath
        }
      })
    }
  } else {
    next()
  }

})

export default router
