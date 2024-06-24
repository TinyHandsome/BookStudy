import { defineStore } from 'pinia'
import { ref } from 'vue'

// 第一个参数是唯一的store id
const useTabbarStore = defineStore("tabbar", () => {
    const isTabbarShow = ref(true)
    const change = (value) => {
        isTabbarShow.value = value
    }

    return {
        isTabbarShow,
        change
    }
})


export default useTabbarStore