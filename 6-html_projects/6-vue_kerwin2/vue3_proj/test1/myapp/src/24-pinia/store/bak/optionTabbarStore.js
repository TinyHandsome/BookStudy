import { defineStore } from 'pinia'

// 第一个参数是唯一的store id
const useTabbarStore = defineStore("tabbar", {
    // state: () => {
    //     return {
    //         isTabbarShow: true,
    //     }
    // }
    // 简写
    state: () => ({
        isTabbarShow: true,
    }),
    actions: {
        change(value){
            this.isTabbarShow = value
        }
    }
})


export default useTabbarStore