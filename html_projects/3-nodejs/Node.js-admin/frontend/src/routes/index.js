import SMERouter from 'sme-router'

const router = new SMERouter('root')


import index from '../controllers/index'
import signin from '../controllers/signin'

// 路由守卫
router.use((req) => {
    // 第一个打开的界面
    $.ajax({
        url: '/api/users/isAuth',
        dataType: 'json',
        headers: {
            'X-Access-Token': localStorage.getItem('lg-token') || ''
        },
        success(result) {
            if (result.ret) {
                router.go('/index')
            } else {
                router.go('/signin')
            }
        }
    })
})

router.route('/', () => { })
router.route('/signin', signin(router))
router.route('/index', index(router))

// router.route('/signin', signin(router))

export default router