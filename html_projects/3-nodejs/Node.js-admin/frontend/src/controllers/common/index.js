import * as removeModel from '../../models/remove'
import page from '../../databus/page'

const remove = ({
    $box,
    url,
    loadData,
    length
}) => {
    // 【删除事件绑定】通过绑定代理，将父级的点击事件给子级
    $box.off('click').on('click', '.remove', async function () {
        // let result = await removeModel.remove($(this).data('id'))
        let result = await removeModel.remove({
            url,
            id: $(this).data('id')
        })
        if (result.ret) {
            loadData()
            
            const isLastPage = Math.ceil(length / page.pageSize) === page.curPage
            const restOne = length % page.pageSize === 1
            const notPageFirtst = page.curPage > 0
            
            if (restOne && isLastPage && notPageFirtst) {
                page.setCurPage(page.curPage - 1)
            }
            
            length --
        }
    })
}

export {
    remove
}