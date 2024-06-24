import { defineStore } from 'pinia'
import { ref } from 'vue'

// 第一个参数是唯一的store id
const useCityStore = defineStore("city", () => {
    const cityName = ref("北京")
    const cityId = ref(110100)

    const change = (cn, ci) => {
        cityName.value = cn
        cityId.value = ci
    }

    return {
        cityName,
        cityId,
        change
    }
})


export default useCityStore