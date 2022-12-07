import page from '../../databus/page'
import usersAddTpl from '../../views/users-addUser.art'


// 添加用户
export const addUser = () => {
    const html = usersAddTpl()
    $('#users-list-box').after(html)

    // 提交表单
    const _save = () => {
        const data = $('#users-form').serialize()
        $.ajax({
            // url: 'http://localhost:3000/api/users/signup',
            url: '/api/users',
            type: 'post',
            headers: {
                'X-Access-Token': localStorage.getItem('lg-token') || ''
            },
            data: data,
            success: (res) => {
                // console.log(res);
                // 添加数据后渲染
                page.setCurPage(1)

                // 告知list页面要重新渲染
                $('body').trigger('addUser')
                // _loadData()
            },
            error: (res) => {
                console.log(res);
            }
        })

        // 点击关闭模态框
        const $btnClose = $('#users-close')
        $btnClose.click()
    }

    // 点击保存，提交表单
    $('#users-save').on('click', _save)
}
