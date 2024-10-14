import { defineStore } from 'pinia'
import { ref } from 'vue'

// 第一个参数是唯一的store id
const useNewsStore = defineStore("news", () => {
    const list = ref([])
    const add = (value) => {
        list.value.push({...value})
    }

    return {
        list,
        add
    }
})


export default useNewsStore