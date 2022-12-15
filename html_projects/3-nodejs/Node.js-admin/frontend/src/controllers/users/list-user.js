import usersTpl from '../../views/users.art'
import usersListTpl from '../../views/users-list.art'
import pagination from '../../components/pagination'
import page from '../../databus/page'

import { addUser } from './add-user'
import { usersList as usersListModel } from '../../models/users-list'
import { auth as authModel } from '../../models/auth'
import { usersRemove as usersRemoveModel } from '../../models/users-remove'

let curPage = page.curPage
let pageSize = page.pageSize

let dataList = []


// 从后端加载数据
const _loadData = async () => {
    let result = await usersListModel()
    dataList = result.data
    // 分页
    pagination(result.data, pageSize, curPage)
    // 数据渲染
    _list(curPage)
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
    $('#users-list').on('click', '.remove', async function () {
        let result = await usersRemoveModel($(this).data('id'))
        if(result.ret){
            _loadData()
    
            const isLastPage = Math.ceil(dataList.length / pageSize) === page.curPage
            const restOne = dataList.length % pageSize === 1
            const notPageFirtst = page.curPage > 0
    
            if (restOne && isLastPage && notPageFirtst) {
                page.setCurPage(page.curPage - 1)
            }
        }
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

    const loadIndex = (res, next) => {
        // 填充用户列表
        // $('#content').html(usersTpl())
        next()
        res.render(usersTpl({}))

        $('#add-user-btn').on('click', addUser)
        // 初次渲染list
        _loadData()

        // 页面事件绑定
        _methods()

        // 订阅事件
        _subscribe()
    }

    return async (req, res, next) => {
        let result = await authModel()
        if (result.ret) {
            loadIndex(res, next)
        } else {
            router.go('/signin')
        }
    }
}

export default index