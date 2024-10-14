import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import Films from '../views/Films.vue'
// import Cinemas from '../views/Cinemas.vue'
// import Center from '../views/Center.vue'

import NotFound from '../views/NotFound.vue'
import Detail from '../views/Detail.vue'
import NowplayingVue from '../views/films/Nowplaying.vue'
import Comingsoon from '../views/films/Comingsoon.vue'
import Login from '../views/Login.vue'
import City from '../views/City.vue'

import AddNews from '../views/AddNews.vue'
import NewsList from '../views/NewsList.vue'

const routes = [

    // 重定向和起别名
    {
        path: "/",
        // redirect: "/films"
        redirect: {
            name: "c"
        }
    },
    {
        path: "/films",
        component: Films,
        // redirect: { name: "np" },
        redirect: "/films/nowplaying",
        children: [
            {
                path: "/films/nowplaying",
                component: NowplayingVue,
                name: "np"
            },
            {
                path: "comingsoon",
                component: Comingsoon
            }
        ]
    },
    // 配置detail
    {
        path: '/detail/:filmId',
        component: Detail,
    },
    {
        path: "/cinemas",
        component: () => import('../views/Cinemas.vue'),
        name: "c"
    },
    {
        path: "/center",
        alias: "/wode",
        component: () => import('../views/Center.vue'),
        meta: {
            requiredAuth: true
        },
    },
    {
        path: "/home",
        component: () => import('../views/Home.vue'),
        children: [
            {
                path: "/news/addnews",
                component: AddNews
            },
            {
                path: "/news/newslist",
                component: NewsList
            },
        ]
    },
    // Login
    {
        path: "/login",
        name: "Login",
        component: Login
    },
    {
        path: "/city",
        component: City
    },


    // 其他匹配，pathMatch只是占位符，可以随便取名，(.*)*通配符：随便什么符号都行，且重复n次
    {
        path: '/:pathMatch(.*)*',
        component: NotFound
    },
]

const router = createRouter({
    // history: createWebHashHistory(),
    history: createWebHistory(),
    routes, // routes: routes的缩写
})

// 全局拦截
router.beforeEach((to, from, next) => {
    let isAuthenticated = localStorage.getItem("token")
    if (to.name !== 'Login' && !isAuthenticated) next({ name: 'Login' })
    else next()
})

export default router