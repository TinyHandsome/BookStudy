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
import { Toast } from "vant";


const http = axios.create({
    baseURL: "https://m.maizuo.com",
    timeout: 10000,
    headers: {
        "X-Client-Info":
            '{"a":"3000","ch":"1002","v":"5.2.1","e":"1689149181904756335738881"}',
        // "X-Host": "mall.film-ticket.film.list",
    },
})

// 添加请求拦截器
http.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    Toast.loading({
        message: "加载中...",
        forbidClick: true,
        duration: 0,
    });
    return config;
}, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
});

// 添加响应拦截器
http.interceptors.response.use(function (response) {
    // 对响应数据做点什么

    // 隐藏加载
    Toast.clear();
    return response;
}, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
});

export default http