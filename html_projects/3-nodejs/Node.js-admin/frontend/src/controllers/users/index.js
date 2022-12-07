import indexTpl from '../../views/index.art'
import usersTpl from '../../views/users.art'
import usersListTpl from '../../views/users-list.art'
import pagination from '../../components/pagination'
import page from '../../databus/page'

import { addUser } from './add-user'

let curPage = page.curPage
let pageSize = page.pageSize

const htmlIndex = indexTpl({})
let dataList = []



// 从后端加载数据
const _loadData = () => {
    $.ajax({
        url: '/api/users',
        headers: {
            'X-Access-Token': localStorage.getItem('lg-token') || ''
        },
        // async: false,
        success(result) {
            dataList = result.data
            // 分页
            pagination(result.data, pageSize, curPage)
            // 数据渲染
            _list(curPage)
        }
    })
}

// 获取列表数据，并把结果放到html中
const _list = (pageNo) => {
    let start = (pageNo - 1) * pageSize
    $('#users-list').html(usersListTpl({
        data: dataList.slice(start, start + pageSize)
    }))
}

const _methods = () => {
    // 【删除事件绑定】通过绑定代理，将父级的点击事件给子级
    $('#users-list').on('click', '.remove', function () {
        $.ajax({
            url: '/api/users',
            type: 'delete',
            headers: {
                'X-Access-Token': localStorage.getItem('lg-token') || ''
            },
            data: {
                id: $(this).data('id')
            },
            success: () => {
                _loadData()

                const isLastPage = Math.ceil(dataList.length / pageSize) === page.curPage
                const restOne = dataList.length % pageSize === 1
                const notPageFirtst = page.curPage > 0

                if (restOne && isLastPage && notPageFirtst) {
                    page.setCurPage(page.curPage - 1)
                }
            }
        })
    })

    // 【登出事件绑定】
    $('#users-signout').on('click', (e) => {
        e.preventDefault()
        // router.go('/signin')
        localStorage.setItem('lg-token', '')
        location.reload()

        // $.ajax({
        //     url: '/api/users/signout',
        //     dataType: 'json',
        //     headers: {
        //         'X-Access-Token': localStorage.getItem('lg-token') || ''
        //     },
        //     success(result) {
        //         if (result.ret) {
        //             location.reload()
        //         }
        //     }
        // })
    })
}

const _subscribe = () => {
    $('body').on('changeCurPage', () => {
        _list(page.curPage)
        // console.log(page.curPage);
    })
    $('body').on('addUser', () => {
        _loadData()
    })
}

const index = (router) => {

    const loadIndex = (res) => {
        // 渲染首页        
        res.render(htmlIndex)

        // 让页面撑满整个屏幕
        $(window, '.wrapper').resize()

        // 填充用户列表
        $('#content').html(usersTpl())
        $('#add-user-btn').on('click', addUser)
        // 初次渲染list
        _loadData()

        // 页面事件绑定
        _methods()

        // 订阅事件
        _subscribe()
    }

    return (req, res, next) => {
        $.ajax({
            url: '/api/users/isAuth',
            dataType: 'json',
            headers: {
                'X-Access-Token': localStorage.getItem('lg-token') || ''
            },
            async: false,
            success(result) {
                if (result.ret) {
                    loadIndex(res)
                } else {
                    router.go('/signin')
                }
            }
        })
    }
}

export default index