// import SMERouter from 'sme-router'
import GP21Router from 'gp21-router'

const router = new GP21Router('root')


import index from '../controllers/index'
import listUser from '../controllers/users/list-user'
import signin from '../controllers/signin'
import { auth as authModel } from '../models/auth'
import listPosition from '../controllers/positions/list-position'

// 路由守卫
router.use(async (req) => {
    const url = req.url
    // 第一个打开的界面
    let result = await authModel()

    if (result.ret) {
        router.go(url)
    } else {
        router.go('/signin')
    }
})

// router.route('/', () => { })
router.route('/signin', signin(router))
router.route('/index', index(router))
router.route('/index/users', listUser(router))
router.route('/index/positions', listPosition(router))

router.route('*', (req, res, next) => {
    res.redirect('/index/users')
})

// router.route('/signin', signin(router))

export default router