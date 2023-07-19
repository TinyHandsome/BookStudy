// 对于数据请求的封装
// 1
// import axios from "axios"
// function http() {
//     return axios({
//         url: "https://m.maizuo.com/gateway?cityId=440300&pageNum=1&pageSize=10&type=1&k=3602463",
//         headers: {
//             "X-Client-Info":
//                 '{"a":"3000","ch":"1002","v":"5.2.1","e":"1689149181904756335738881"}',
//             "X-Host": "mall.film-ticket.film.list",
//         },
//     })
// }

// export default http

import axios from "axios"
const http = axios.create({
    baseURL: "https://m.maizuo.com",
    timeout: 10000,
    headers: {
        "X-Client-Info":
            '{"a":"3000","ch":"1002","v":"5.2.1","e":"1689149181904756335738881"}',
        // "X-Host": "mall.film-ticket.film.list",
    },
})

export default http