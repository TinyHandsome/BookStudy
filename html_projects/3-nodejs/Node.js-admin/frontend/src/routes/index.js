import SMERouter from 'sme-router'

const router = new SMERouter('root')


import { signin, index } from '../controllers'

router.use((req) => {
    // 第一个打开的界面
    $.ajax({
        url: '/api/users/isAuth',
        dataType: 'json',
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