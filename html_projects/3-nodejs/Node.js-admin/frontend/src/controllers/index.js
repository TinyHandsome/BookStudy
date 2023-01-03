import indexTpl from '../views/index.art'
import { auth as authModel } from '../models/auth'
import pageHeader from '../components/pageheader'

import img from '../assets/user2-160x160.jpg'

const index = (router) => {
    return async (req, res, next) => {
        let result = await authModel()
        if (result.ret) {
            const html = indexTpl({
                subRouter: res.subRoute(),
                img
            })
            // 渲染首页        
            next(html)
            // 让页面撑满整个屏幕
            $(window, '.wrapper').resize()

            // 加载页面导航栏
            pageHeader()


            // $lis.on('click', function () {
            //     const url = $(this).attr('to')
            //     router.go(url)
            // })

            const $as = $('#sidebar-menu li:not(:first-child) a')
            // let hash = location.hash.slice(1)
            let hash = location.hash
            // $as.find(`[href="${hash}"]`).parent().addClass('active').siblings().removeClass('active')
            // console.log($as.eq(0).attr('href'));
            $as.filter(`[href="${hash}"]`).parent().addClass('active').siblings().removeClass('active');

        } else {
            router.go('/signin')
        }
    }
}

export default index