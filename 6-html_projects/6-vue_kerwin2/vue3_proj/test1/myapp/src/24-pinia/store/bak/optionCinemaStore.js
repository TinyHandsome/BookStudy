import { defineStore } from "pinia";
import axios from 'axios';


const useCinemaStore = defineStore("cinema", {
    // options store
    state: () => ({
        cinemaList: []
    }),
    actions: {
        // 不要写成箭头函数，因为箭头函数中的this指向的不是本对象，而是windows
        async getCinemaList() {
            console.log("ajax");
            var res = await axios({
                url: "https://m.maizuo.com/gateway?cityId=110100&ticketFlag=1&k=5385023",
                headers: {
                    "X-Client-Info":
                        '{"a":"3000","ch":"1002","v":"5.2.1","e":"1701324144895711134613505"}',
                    "X-Host": "mall.film-ticket.cinema.list",
                },
            })
            // 提交mutation
            // store.commit("changeCinemaList", res.data.data.cinemas)
            console.log(res.data.data);
            this.cinemaList = res.data.data.cinemas
        }
    },
    getters: {
        filterCinemaList(state) {
            return (type) =>
                state.cinemaList.filter(item => item.eTicketFlag === type)
        }
    }
})

export default useCinemaStore