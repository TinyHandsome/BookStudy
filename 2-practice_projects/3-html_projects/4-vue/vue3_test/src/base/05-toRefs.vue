<template>
    <div>
        {{ myname }}
        <button @click="handleClick">change</button>
    </div>
</template>

<script>
import { reactive, toRefs } from 'vue'
export default {
    setup() {
        console.log("setup");

        // 定义状态
        const obj = reactive({
            myname: "kerwin",
            myage: 100
        })
        const handleClick = () => {
            obj.myname = "liyingjun"
        }

        return {
            handleClick,
            ...toRefs(obj)
        }
    }
}
</script>