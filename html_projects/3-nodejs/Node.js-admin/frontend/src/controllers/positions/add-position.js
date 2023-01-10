import page from '../../databus/page'
import positionsAddTpl from '../../views/positions-add.art'
import { positionsAdd } from '../../models/positions'

// 添加职位
export const addPosition = () => {
    $('#positions-list-box').after(positionsAddTpl())

    // 提交表单
    const _save = async () => {

        const data = $('#position-form').serialize()
        let result = await positionsAdd(data)
        if (result.ret) {
            // 添加数据后渲染
            page.setCurPage(1)
            // 告知list页面要重新渲染
            $('body').trigger('addPosition')
            // _loadData()
        }
        // 点击关闭模态框
        const $btnClose = $('#positions-close')
        $btnClose.click()
    }

    // 点击保存，提交表单
    $('#positions-save').off('click').on('click', _save)
}
