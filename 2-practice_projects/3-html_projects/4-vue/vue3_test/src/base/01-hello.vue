<template>
    <div>
        hello3 新写法
        {{ obj.myname }}
        <button @click="handleClick">change</button>
    </div>
</template>

<script>
import { reactive } from 'vue'
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
            obj,
            handleClick
        }
    }
}
</script>