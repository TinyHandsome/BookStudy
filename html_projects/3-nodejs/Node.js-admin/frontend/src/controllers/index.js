import indexTpl from '../views/index.art'
import usersTpl from '../views/users.art'
import usersListTpl from '../views/users-list.art'
import pagination from '../components/pagination'

let curPage = 1
const pageSize = 10

const htmlIndex = indexTpl({})
let dataList = []


// 注册
const _signup = () => {
    const $btnClose = $('#users-close')

    // 提交表单
    const data = $('#users-form').serialize()
    $.ajax({
        // url: 'http://localhost:3000/api/users/signup',
        url: '/api/users',
        type: 'post',
        data: data,
        success: (res) => {
            // console.log(res);
            // 添加数据后渲染
            _loadData()
        },
        error: (res) => {
            console.log(res);
        }
    })

    $btnClose.click()
}

// 从后端加载数据
const _loadData = () => {
    $.ajax({
        url: '/api/users',
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
            data: {
                id: $(this).data('id')
            },
            success: () => {
                _loadData()

                if (dataList.length % pageSize === 1 && Math.ceil(dataList.length / pageSize) === curPage && curPage > 0) {
                    curPage--
                }
            }
        })
    })

    // 【登出事件绑定】
    $('#users-signout').on('click', (e) => {
        e.preventDefault()
        // router.go('/signin')
        $.ajax({
            url: '/api/users/signout',
            dataType: 'json',
            success(result) {
                if (result.ret) {
                    location.reload()
                }
            }
        })
    })

    // 点击保存，提交表单
    $('#users-save').on('click', _signup)
}

const _subscribe = () => {
    $.on('changeCurPage', () => {
        console.log(0);
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