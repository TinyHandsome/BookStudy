import indexTpl from '../views/index.art'
import signinTpl from '../views/signin.art'
import usersTpl from '../views/users.art'
import usersListTpl from '../views/users-list.art'
import usersListPageTpl from '../views/users-pages.art'

const htmlIndex = indexTpl({})
const htmlSignin = signinTpl({})
const pageSize = 10

let curPage = 1
let dataList = []


const _handleSubmit = (router) => {
    return (e) => {
        e.preventDefault();
        router.go('/index')
    }
}

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
            _list(curPage)
        },
        error: (res) => {
            console.log(res);
        }
    })

    $btnClose.click()
}

const _pagination = (data) => {
    const total = data.length
    const pageCount = Math.ceil(total / pageSize)
    const pageArray = new Array(pageCount)

    const htmlPage = usersListPageTpl({
        pageArray
    })

    $('#users-page').html(htmlPage)

    // 第一页实现高亮
    // $('#users-page-list li:nth-child(2)').addClass('active')
    _setPageActive(curPage)
}

const _loadData = () => {
    $.ajax({
        url: '/api/users',
        // async: false,
        success(result) {
            dataList = result.data
            // 分页
            _pagination(result.data)
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

const signin = (router) => {
    return (req, res, next) => {
        res.render(htmlSignin)
        $('#signin').on('submit', _handleSubmit(router))
    }
}

const _setPageActive = (index) => {
    $('#users-page #users-page-list li:not(:first-child, :last-child)')
        .eq(index - 1)
        .addClass('active')
        .siblings()
        .removeClass('active')
}

const signup = () => { }

const index = (router) => {
    return (req, res, next) => {
        res.render(htmlIndex)

        // 让页面撑满整个屏幕
        $(window, '.wrapper').resize()

        // 填充用户列表
        $('#content').html(usersTpl())
        // 【删除】通过绑定代理，将父级的点击事件给子级
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
        // 实现其他页点击事件的高亮
        $('#users-page').on('click', '#users-page-list li:not(:first-child, :last-child)', function () {
            const index = $(this).index()
            // console.log($(this).index());
            _list(index)
            curPage = index
            _setPageActive(index)
        })
        // 绑定上一页下一页逻辑
        $('#users-page').on('click', '#users-page-list li:last-child', function () {
            if (curPage < Math.ceil(dataList.length / pageSize)) {
                curPage++
                _list(curPage)
                _setPageActive(curPage)
            }
        })
        $('#users-page').on('click', '#users-page-list li:first-child', function () {
            if (curPage > 1) {
                curPage--
                _list(curPage)
                _setPageActive(curPage)
            }
        })

        // 初次渲染list
        _loadData()

        // 点击保存，提交表单
        $('#users-save').on('click', _signup)
    }
}

export {
    signin,
    signup,
    index
}