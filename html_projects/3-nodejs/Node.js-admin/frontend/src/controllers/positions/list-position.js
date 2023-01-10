// export default (router) => {
//     return (req, res, next) => {
//         next()
//         res.render('position')
//     }
// }


import { auth as authModel } from "../../models/auth";
import positionsTpl from '../../views/positions.art'
import pagination from '../../components/pagination'
import positionsListTpl from '../../views/positions-list.art'
import { positionList} from "../../models/positions";
import page from "../../databus/page";

import { addPosition } from "./add-position";

let pageSize = page.pageSize
let curPage = page.curPage
let dataList = []

// 获取列表数据，并把结果放到html中
const _list = (pageNo) => {
    let start = (pageNo - 1) * pageSize
    $('#positions-list').html(positionsListTpl({
        data: dataList.slice(start, start + pageSize)
    }))
}

const _loadData = async () => {
    let list = await positionList()
    dataList = list
    // 分页
    pagination(dataList)
    // 数据渲染
    _list(curPage)
}

const _subscribe = () => {
    $('body').off('changeCurPage').on('changeCurPage', () => {
        _list(page.curPage)
        // console.log(page.curPage);
    })
    $('body').off('addPosition').on('addPosition', () => {
        _loadData()
    })
}

const listPositions = (router) => {
    return async (req, res, next) => {
        let result = await authModel()
        if (result.ret) {
            next()
            res.render(positionsTpl())

            // 初次渲染list
            _loadData()
            // 订阅事件
            _subscribe()
            // 点击添加职位
            addPosition()

           
        } else {
            router.go('/signin')
        }
    }
}

export default listPositions