import {createStore} from 'vuex'
import { CHANGE_TABBAR } from './type'

import axios from 'axios'

const store = createStore({
    state(){
        return {
            isTabbarShow: true,
            cinemaList: [],
        }
    },
    // 唯一修改状态的位置
    mutations: {
        // showTabbar(state){
        //     state.isTabbarShow = true
        // },
        // hideTabbar(state){
        //     state.isTabbarShow = false
        // },
        [CHANGE_TABBAR](state, payload){
            state.isTabbarShow = payload
        },
        changeCinemaList(state, payload){
            state.cinemaList = payload
        }
    },
    // 同步+异步
    actions: {
        async getCinemaList(store){
            console.log("ajax");
            var res = await axios({
                url: "https://m.maizuo.com/gateway?cityId=110100&ticketFlag=1&k=5385023",
                headers: {
                    "X-Client-Info":
                        '{"a":"3000","ch":"1002","v":"5.2.1","e":"1701324144895711134613505"}',
                    "X-Host": "mall.film-ticket.cinema.list",
                },
            })
            // console.log(res.data.data.cinemas);
            // 提交mutation
            store.commit("changeCinemaList", res.data.data.cinemas)
        }
    }
})

export default store