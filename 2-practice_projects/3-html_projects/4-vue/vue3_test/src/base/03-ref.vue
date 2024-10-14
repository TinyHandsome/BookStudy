<template>
    <div>
        hello3 新写法
        {{ myname }}
        <button @click="handleClick">change</button>
    </div>
</template>

<script>
import { ref } from 'vue'
export default {
    setup() {

        // 定义状态
        const myname = ref("default name")
        console.log(myname);

        const handleClick = () => {
            myname.value = "liyingjun"
        }

        return {
            myname,
            handleClick
        }
    }
}
</script>