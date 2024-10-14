import { createRouter, createWebHashHistory } from 'vue-router'
import Film from '@/views/Film'
import NowPlaying from '@/views/films/NowPlaying'
import ComingSoon from '@/views/films/ComingSoon'
import Cinema from '@/views/Cinema'
import Center from '@/views/Center'
import Detail from '@/views/Detail'

const routes = [
  {
    path: '/films',
    component: Film,
    name: 'films',
    children: [
      {
        path: '/films',
        redirect: {
          name: 'nowplaying'
        }
      },
      {
        path: '/films/nowplaying',
        component: NowPlaying,
        name: 'nowplaying'
      },
      {
        path: '/films/comingsoon',
        component: ComingSoon,
        name: 'commingsoon'
      },
    ]
  },
  {
    path: '/cinemas',
    component: Cinema
  },
  {
    path: '/center',
    component: Center
  },
  {
    path: '/detail/:id',
    component: Detail
  },
  {
    path: '/',
    redirect: '/films'
  },
  {
    path: '/:anyasdfasdfasdf',
    redirect: {
      name: 'nowplaying'
    }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
