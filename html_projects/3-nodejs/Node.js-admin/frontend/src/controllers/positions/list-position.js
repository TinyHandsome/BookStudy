// export default (router) => {
//     return (req, res, next) => {
//         next()
//         res.render('position')
//     }
// }


import { auth as authModel } from "../../models/auth";
import positionsTpl from '../../views/positions.art'
import positionsAddTpl from '../../views/positions-add.art'
import pagination from '../../components/pagination'
import positionsListTpl from '../../views/positions-list.art'
import { positionList } from "../../models/positions-list";

const listPositions = (router) => {
    console.log('object');
    return async (req, res, next) => {
        let result = await authModel()
        if(result.ret){
            next()
            res.render(positionsTpl())

            const list = await positionList()
            console.log(list);

            // 渲染list
            $('#positions-list').html(positionsListTpl({
                data: list
            }))
            
            // 分页
            pagination(list)

            // 职位添加
            $('#positions-list-box').after(positionsAddTpl())
            $('#positions-save').off('click').on('click', () => {
                const formbody = $('#position-form').serialize()
                // console.log(formbody);

                $('#positions-close').click()
            })

        } else {
            router.go('/signin')
        }
    }
}

export default listPositions