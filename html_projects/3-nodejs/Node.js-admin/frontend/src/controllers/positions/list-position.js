// export default (router) => {
//     return (req, res, next) => {
//         next()
//         res.render('position')
//     }
// }


import { auth as authModel } from "../../models/auth";
const listPositions = (router) => {
    console.log('object');
    return async (req, res, next) => {
        let result = await authModel()
        if(result.ret){
            next()
            res.render('postions.')
        } else {
            router.go('/signin')
        }
    }
}

export default listPositions