import {createRouter, createWebHashHistory} from 'vue-router'
import Films from '../views/Films.vue'
import Cinemas from '../views/Cinemas.vue'
import Center from '../views/Center.vue'
import NotFound from '../views/NotFound.vue'
import NowplayingVue from 'myapp/src/12-作用域插槽/Nowplaying.vue'

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
        children: [
            {
                path: "/films/nowplaying",
                component: NowplayingVue
            },
            {
                path: "/films/comingsoon",
                component: ComingSoon
            }
        ]
    },
    {
        path: "/cinemas",
        component: Cinemas,
        name: "c"
    },
    {
        path: "/center",
        alias: "/wode",
        component: Center
    },
    // 其他匹配，pathMatch只是占位符，可以随便取名，(.*)*通配符：随便什么符号都行，且重复n次
    {
        path: '/:pathMatch(.*)*', 
        component: NotFound
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes, // routes: routes的缩写
})

export default router