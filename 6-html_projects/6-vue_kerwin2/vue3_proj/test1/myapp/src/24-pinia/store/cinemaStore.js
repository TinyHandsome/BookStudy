import { defineStore } from "pinia";
import axios from 'axios';
import { ref, computed } from 'vue'
import useCityStore from "./cityStore";

// 引入另一个store
const cityStore = useCityStore()

const useCinemaStore = defineStore("cinema", () => {
    // options store
    const cinemaList = ref([])
    const getCinemaList = async () => {
        console.log("ajax");
        var res = await axios({
            url: `https://m.maizuo.com/gateway?cityId=${cityStore.cityId}&ticketFlag=1&k=5385023`,
            headers: {
                "X-Client-Info":
                    '{"a":"3000","ch":"1002","v":"5.2.1","e":"1701324144895711134613505"}',
                "X-Host": "mall.film-ticket.cinema.list",
            },
        })
        console.log(res.data.data);
        cinemaList.value = res.data.data.cinemas
    }
    const filterCinemaList = computed(() => {
        return (type) =>
            cinemaList.value.filter(item => item.eTicketFlag === type)
    })

    const clearCinemaList = () => {
        cinemaList.value = []
    }

    return {
        cinemaList,
        getCinemaList,
        filterCinemaList,
        clearCinemaList
    }
})

export default useCinemaStore