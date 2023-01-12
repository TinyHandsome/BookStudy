import usersTpl from '../../views/users.art'
import usersListTpl from '../../views/users-list.art'
import pagination from '../../components/pagination'
import page from '../../databus/page'

import { addUser } from './add-user'
import { usersList as usersListModel } from '../../models/users-list'
import { auth as authModel } from '../../models/auth'

import { remove } from '../common'

let curPage = page.curPage
let pageSize = page.pageSize

let state = {
    list: []
}


// 从后端加载数据
const _loadData = async () => {
    let result = await usersListModel()

    state.list = result.data

    // 分页
    pagination(result.data)
    // 数据渲染
    _list(curPage)
}

// 获取列表数据，并把结果放到html中
const _list = (pageNo) => {
    let start = (pageNo - 1) * pageSize
    $('#users-list').html(usersListTpl({
        data: state.list.slice(start, start + pageSize)
    }))
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
    return async (req, res, next) => {

        let result = await authModel()
        if (result.ret) {
            // 填充用户列表
            // $('#content').html(usersTpl())
            next()
            res.render(usersTpl())

            $('#add-user-btn').on('click', addUser)
            // 初次渲染list
            await _loadData()

            // 页面事件绑定
            remove({
                $box: $('#users-list'),
                // 传递一个引用类型的值 state，在删除组件里能实时获取数据条数
                state,
                url: '/api/users',
                loadData: _loadData
            })

            // 订阅事件
            _subscribe()
        } else {
            router.go('/signin')
        }
    }

    // return async (req, res, next) => {
    //     let result = await authModel()
    //     if (result.ret) {
    //         loadIndex(res, next)
    //     } else {
    //         router.go('/signin')
    //     }
    // }
}

export default index