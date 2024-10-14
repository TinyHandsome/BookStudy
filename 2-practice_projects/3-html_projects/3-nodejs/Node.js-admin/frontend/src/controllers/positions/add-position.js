import page from '../../databus/page'
import positionsAddTpl from '../../views/positions-add.art'
import { positionsAdd } from '../../models/positions'

// 添加职位
export const addPosition = () => {
    $('#positions-list-box').after(positionsAddTpl())

    // 提交表单
    const _save = async () => {

        // const data = $('#position-form').serialize()

        try {
            let result = await positionsAdd()

            if (result.ret) {
                page.setCurPage(1)
                // 告知list页面要重新渲染
                $('body').trigger('addPosition')
                // _loadData()
            }
            // 点击关闭模态框
            const $btnClose = $('#positions-close')
            $btnClose.click()
        } catch (err) {
            console.log(err);
        }
    }

    // 点击保存，提交表单
    $('#positions-save').off('click').on('click', _save)
}
