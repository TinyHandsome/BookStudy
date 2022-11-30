import usersListPageTpl from '../views/users-pages.art'

// 【分页事件绑定】实现其他页点击事件的高亮
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

const pagination = (data) => {
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

const _setPageActive = (index) => {
    $('#users-page #users-page-list li:not(:first-child, :last-child)')
        .eq(index - 1)
        .addClass('active')
        .siblings()
        .removeClass('active')
}


export default pagination