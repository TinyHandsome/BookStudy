import usersListPageTpl from '../views/users-pages.art'
import page from '../databus/page'

const pageSize = page.pageSize

const _bindEvent = (data) => {
    // 【分页事件绑定】实现其他页点击事件的高亮
    $('#users-page').off('click').on('click', '#users-page-list li:not(:first-child, :last-child)', function () {
        const index = $(this).index()
        // console.log($(this).index());
        // _list(index)
        // curPage = index

        page.setCurPage(index)
        $('body').trigger('changeCurPage')

        _setPageActive(index)
        console.log('index: ', page.curPage);
    })

    // 绑定上一页下一页逻辑
    $('#users-page').on('click', '#users-page-list li:first-child', function () {
        console.log('before: ', page.curPage);
        if (page.curPage > 1) {
            page.setCurPage(page.curPage - 1)
            $('body').trigger('changeCurPage')

            _setPageActive(page.curPage)
        }
        console.log('after: ', page.curPage);
    })

    $('#users-page').on('click', '#users-page-list li:last-child', function () {
        console.log('before: ', page.curPage);
        if (page.curPage < Math.ceil(data.length / pageSize)) {

            page.setCurPage(page.curPage + 1)
            $('body').trigger('changeCurPage')
            _setPageActive(page.curPage)
        }
        console.log('after: ', page.curPage);
    })


}

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
    _setPageActive(page.curPage)

    // 绑定事件
    _bindEvent(data, pageSize)
}

const _setPageActive = (index) => {
    $('#users-page #users-page-list li:not(:first-child, :last-child)')
        .eq(index - 1)
        .addClass('active')
        .siblings()
        .removeClass('active')
}


export default pagination