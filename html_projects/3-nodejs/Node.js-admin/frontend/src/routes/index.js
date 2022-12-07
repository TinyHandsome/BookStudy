import SMERouter from 'sme-router'

const router = new SMERouter('root')


import index from '../controllers/users/index'
import signin from '../controllers/signin'
import { routerGuard as rgModel } from '../models/router-guard'

// 路由守卫
router.use(async (req) => {
    // 第一个打开的界面
    let result = await rgModel()

    if (result.ret) {
        router.go('/index')
    } else {
        router.go('/signin')
    }
})

router.route('/', () => { })
router.route('/signin', signin(router))
router.route('/index', index(router))

// router.route('/signin', signin(router))

export default router