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

const listPositions = (router) => {
    console.log('object');
    return async (req, res, next) => {
        let result = await authModel()
        if(result.ret){
            next()
            res.render(positionsTpl())

            $('#positions-list-box').after(positionsAddTpl())

            pagination(['a', 'b', 'c', 'd'], 3)

            $('#positions-save').off('click').on('click', () => {
                const formbody = $('#position-form').serialize()
                console.log(formbody);

                $('#positions-close').click()
            })

        } else {
            router.go('/signin')
        }
    }
}

export default listPositions