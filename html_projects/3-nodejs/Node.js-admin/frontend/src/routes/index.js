import SMERouter from 'sme-router'

const router = new SMERouter('root')


import { signin, index } from '../controllers'

router.route('/signin', signin(router))

router.route('/index', index(router))

// router.route('/signin', signin(router))

export default router