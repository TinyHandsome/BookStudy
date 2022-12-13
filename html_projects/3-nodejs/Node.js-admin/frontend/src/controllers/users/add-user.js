import page from '../../databus/page'
import usersAddTpl from '../../views/users-addUser.art'
import { usersAdd as usersAddModel } from '../../models/users-add'


// 添加用户
export const addUser = () => {
    const html = usersAddTpl()
    $('#users-list-box').after(html)

    // 提交表单
    const _save = async () => {
        const data = $('#users-form').serialize()
        let result = await usersAddModel(data)
        if (result.ret) {
            // 添加数据后渲染
            page.setCurPage(1)
            // 告知list页面要重新渲染
            $('body').trigger('addUser')
            // _loadData()
        }
        // 点击关闭模态框
        const $btnClose = $('#users-close')
        $btnClos.click()
    }

    // 点击保存，提交表单
    $('#users-save').on('click', _save)
}
