import indexTpl from '../views/index.art'
import signinTpl from '../views/signin.art'
import usersTpl from '../views/users.art'
import usersListTpl from '../views/users-list.art'
import usersListPageTpl from '../views/users-pages.art'

const htmlIndex = indexTpl({})
const htmlSignin = signinTpl({})
const pageSize = 10
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
        url: '/api/users/signup',
        type: 'post',
        data: data,
        async success(res) {
            // console.log(res);
            // 添加数据后渲染
            await _loadData()
            _list(1)
        },
        error(res) {
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
    $('#users-page-list li:nth-child(2)').addClass('active')
    // 实现其他页点击事件的高亮
    $('#users-page-list li:not(:first-child, :last-child)').on('click', function () {
        $(this).addClass('active').siblings().removeClass('active')
        // console.log($(this).index());
        _list($(this).index())
    })
}

const _loadData = () => {
    return $.ajax({
        url: '/api/users/list',
        // async: false,
        success(result) {
            dataList = result.data
            // 分页
            _pagination(result.data)
            _list(1)
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

const signup = () => { }

const index = (router) => {
    return async (req, res, next) => {
        res.render(htmlIndex)

        // 让页面撑满整个屏幕
        $(window, '.wrapper').resize()

        // 填充用户列表
        $('#content').html(usersTpl())

        // 初次渲染list
        await _loadData()
        _list(1)

        // 点击保存，提交表单
        $('#users-save').on('click', _signup)
    }
}

export {
    signin,
    signup,
    index
}